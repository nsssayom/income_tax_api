from app import db
from sqlalchemy.dialects import mysql


class User(db.Model):
    id = db.Column(mysql.BIGINT(20, unsigned=True), primary_key=True)
    name = db.Column(mysql.VARCHAR(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()
