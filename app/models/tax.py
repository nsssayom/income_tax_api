from app import db
from sqlalchemy.dialects import mysql
from datetime import datetime


class User(db.Model):
    id = db.Column(mysql.BIGINT(20, unsigned=True), primary_key=True)
    user_id = db.Column(mysql.BIGINT(20, unsigned=True, unique=True, dnullabe=False))
    year = db.Column(mysql.VARCHAR(70), unique=False, nullable=False)
    collected_at_souce = db.Column(mysql.VARCHAR(20), unique=False, nullable=False)
    advance_paid = db.Column(db.Boolean, unique=False, nullable=False)
    adjustment = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
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
