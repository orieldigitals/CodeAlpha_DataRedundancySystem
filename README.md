# CodeAlpha Internship Project

# Data Redundancy Detection and Management System

## Overview

The **Data Redundancy Detection and Management System** is a web-based application developed as part of the **CodeAlpha Internship Program**. The project addresses one of the most common problems in information systems: the storage of duplicate records that lead to wasted storage, inconsistent information, and poor data quality.

This application intelligently detects duplicate records before they are saved by generating a unique SHA-256 hash from user information and comparing it against existing records in the database. If an identical record already exists, the system prevents duplication and immediately notifies the user.

Beyond duplicate detection, the application also provides a complete record management dashboard with search, editing, deletion, analytics, and export capabilities.

---

# Project Objectives

The primary objectives of this project are to:

* Detect duplicate records before database insertion
* Improve data integrity and consistency
* Reduce unnecessary data redundancy
* Demonstrate practical application of hashing techniques
* Provide a simple and user-friendly management interface

---

# Features

* Duplicate Record Detection
* SHA-256 Hash Generation
* Create New Records
* View Stored Records
* Update Existing Records
* Delete Records
* Search Records
* Dashboard Analytics
* CSV Export
* Responsive User Interface
* Bootstrap-powered Design

---

# Technologies Used

## Backend

* Python
* Flask
* SQLAlchemy
* SQLite

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

# System Workflow

User Input

↓

Generate SHA-256 Hash

↓

Search Database

↓

Duplicate Found?

├── Yes → Display Duplicate Warning

└── No → Save Record Successfully

↓

Update Dashboard

↓

Manage Records

---

# Project Structure

```
CodeAlpha_DataRedundancySystem/

│

├── app.py

├── models.py

├── requirements.txt

├── README.md

├── templates/

│       ├── index.html

│       └── edit.html

├── static/

│       ├── css/

│       └── js/

├── exports/

└── venv/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/orieldigitals/CodeAlpha_DataRedundancySystem.git
```

## Navigate into the project

```bash
cd CodeAlpha_DataRedundancySystem
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Git Bash

```bash
source venv/Scripts/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Screenshots

## Dashboard

(Add Screenshot Here)

---

## Duplicate Detection

(Add Screenshot Here)

---

## Search Functionality

(Add Screenshot Here)

---

## Record Management

(Add Screenshot Here)

---

# Future Improvements

* User Authentication
* Role-Based Access Control
* PDF Report Generation
* Interactive Charts
* Pagination
* Sorting
* REST API
* Docker Deployment
* Cloud Deployment

---

# Learning Outcomes

Through this project, practical experience was gained in:

* Flask Application Development
* Database Design
* SQLAlchemy ORM
* Hashing Algorithms
* Duplicate Detection Techniques
* CRUD Operations
* Bootstrap UI Development
* Git and GitHub Workflow

---

# Author

**Hope Bongnwi**

Developed as part of the **CodeAlpha Internship Program**.

---

# License

This project is developed for educational and portfolio purposes.
