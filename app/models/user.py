from app import db
from sqlalchemy.dialects import mysql
from passlib.hash import pbkdf2_sha256 as sha256
from app import ma
from sqlalchemy import Column
from .income import Income
from .investment import Investment


class User(db.Model):
    __tablename__ = 'user'
    id = Column(mysql.BIGINT(unsigned=True),
                nullable=False, primary_key=True)
    name = Column(mysql.VARCHAR(50), unique=True, nullable=False)
    email = Column(mysql.VARCHAR(50), unique=True, nullable=False)
    phone = Column(mysql.VARCHAR(20), unique=True, nullable=False)
    gender = Column(mysql.BOOLEAN, nullable=True)
    dob = Column(mysql.DATE, nullable=True)
    address = Column(mysql.VARCHAR(255), unique=True, nullable=True)
    is_ff = Column(mysql.BOOLEAN, nullable=True)
    is_disable = Column(mysql.BOOLEAN, nullable=True)
    is_parent_disable = Column(mysql.BOOLEAN, nullable=True)
    joined_on = Column(mysql.DATETIME,
                       server_default=db.func.current_timestamp(),
                       nullable=True)
    is_email_varified = Column(mysql.BOOLEAN, default=False)
    password_hash = Column(mysql.VARCHAR(255), unique=False, nullable=False)

    income = db.relationship(Income, backref="user")
    investment = db.relationship(Investment, backref="user")

    def __init__(self, name, email, phone):
        self.name = name
        self.phone = phone
        self.email = email

    def hash_password(self, password):
        self.password_hash = sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(name=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    gender = ma.auto_field()
    dob = ma.auto_field()
    address = ma.auto_field()
    is_ff = ma.auto_field()
    is_disable = ma.auto_field()
    is_parent_disable = ma.auto_field()
