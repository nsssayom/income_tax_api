from app import db
from sqlalchemy.dialects import mysql
from datetime import datetime


class User(db.Model):
    id = db.Column(mysql.BIGINT(20, unsigned=True), primary_key=True)
    name = db.Column(mysql.VARCHAR(50), unique=False, nullable=False)
    email = db.Column(mysql.VARCHAR(70), unique=False, nullable=False)
    phone = db.Column(mysql.VARCHAR(20), unique=False, nullable=False)
    gender = db.Column(db.Boolean, unique=False, nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    address = db.Column(mysql.VARCHAR(512), unique=False, nullable=False)
    is_ff = db.Column(db.Boolean, unique=False, nullable=False)
    is_disabled = db.Column(db.Boolean, unique=False, nullable=False)
    is_parent_disabled = db.Column(db.Boolean, unique=False, nullable=False)
    joined_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, email, phone, gender, dob, address, is_ff, is_disabled, is_parent_disabled, joined_on):
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.dob = dob
        self.address = address
        self.is_ff = is_ff
        self.is_disabled = is_disabled
        self.is_parent_disabled = is_parent_disabled
        self.joined_on = joined_on
        db.session.add(self)
        db.session.commit()
