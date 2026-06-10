from flask import Flask, render_template, request, redirect, Response
from models import db, DataRecord, compute_hash
from sqlalchemy import or_

import csv
import io

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    message_type = ""

    search = request.args.get("search", "").strip()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        record_hash = compute_hash(name, email, phone)

        existing = DataRecord.query.filter_by(
            data_hash=record_hash
        ).first()

        if existing:
            message = "Duplicate Record Detected!"
            message_type = "danger"

        else:
            new_record = DataRecord(
                name=name,
                email=email,
                phone=phone,
                data_hash=record_hash
            )

            db.session.add(new_record)
            db.session.commit()

            message = "Record Saved Successfully!"
            message_type = "success"

    if search:

        records = DataRecord.query.filter(
            or_(
                DataRecord.name.ilike(f"%{search}%"),
                DataRecord.email.ilike(f"%{search}%"),
                DataRecord.phone.ilike(f"%{search}%")
            )
        ).order_by(DataRecord.id.desc()).all()

    else:
        records = DataRecord.query.order_by(
            DataRecord.id.desc()
        ).all()

    # =========================
    # 🔥 DASHBOARD STATS (FIXED LOCATION)
    # =========================

    total_records = DataRecord.query.count()

    duplicate_attempts = 0

    all_hashes = db.session.query(DataRecord.data_hash).all()
    hash_map = {}

    for h in all_hashes:
        hash_map[h[0]] = hash_map.get(h[0], 0) + 1

    for count in hash_map.values():
        if count > 1:
            duplicate_attempts += (count - 1)

    unique_records = total_records - duplicate_attempts

    last_record = DataRecord.query.order_by(DataRecord.id.desc()).first()
    last_record_name = last_record.name if last_record else "None"

    return render_template(
        "index.html",
        records=records,
        total_records=total_records,
        unique_records=unique_records,
        duplicate_attempts=duplicate_attempts,
        last_record_name=last_record_name,
        message=message,
        message_type=message_type,
        search=search
    )


@app.route("/delete/<int:id>")
def delete(id):

    record = DataRecord.query.get_or_404(id)

    db.session.delete(record)

    db.session.commit()

    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    record = DataRecord.query.get_or_404(id)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        record.name = name
        record.email = email
        record.phone = phone
        record.data_hash = compute_hash(
            name,
            email,
            phone
        )

        db.session.commit()

        return redirect("/")

    return render_template(
        "edit.html",
        record=record
    )

@app.route("/export")
def export():

    records = DataRecord.query.order_by(DataRecord.id.asc()).all()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Name",
        "Email",
        "Phone",
        "Status",
        "Created At"
    ])

    for record in records:
        writer.writerow([
            record.id,
            record.name,
            record.email,
            record.phone,
            record.status,
            record.created_at
        ])

    output.seek(0)

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=records.csv"
        }
    )


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)