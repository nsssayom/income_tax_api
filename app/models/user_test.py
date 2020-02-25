from app import db
from sqlalchemy.dialects import mysql
from passlib.hash import pbkdf2_sha256 as sha256


class User_Test(db.Model):
    __tablename__ = 'users'
    id = db.Column(mysql.BIGINT(20, unsigned=True), primary_key=True, nullable=False)
    name = db.Column(mysql.VARCHAR(50), unique=True, nullable=False)
    password_hash = db.Column(mysql.VARCHAR(255), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name

    def hash_password(self, password):
        self.password_hash = sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(name=username).first()
