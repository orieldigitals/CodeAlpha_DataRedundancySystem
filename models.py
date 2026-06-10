from flask_sqlalchemy import SQLAlchemy
import hashlib
import json

# Initialize SQLAlchemy
db = SQLAlchemy()


class DataRecord(db.Model):
    __tablename__ = "data_records"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200),
        nullable=False
    )

    email = db.Column(
        db.String(200),
        nullable=False
    )

    phone = db.Column(
        db.String(50),
        nullable=False
    )

    data_hash = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="unique"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<DataRecord {self.name}>"


def compute_hash(name, email, phone):
    """
    Generate a SHA256 hash from normalized data.
    """

    payload = json.dumps(
        {
            "name": name.strip().lower(),
            "email": email.strip().lower(),
            "phone": phone.strip()
        },
        sort_keys=True
    )

    return hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()