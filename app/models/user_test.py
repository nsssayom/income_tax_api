from app import db
from sqlalchemy.dialects import mysql
from passlib.apps import custom_app_context as pwd_context


class User_Test(db.Model):
    __tablename__ = 'users'
    id = db.Column(mysql.BIGINT(20, unsigned=True), primary_key=True, nullable=False)
    name = db.Column(mysql.VARCHAR(50), unique=True, nullable=False)
    password_hash = db.Column(mysql.VARCHAR(255), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
