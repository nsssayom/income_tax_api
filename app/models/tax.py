from app import db
from sqlalchemy.dialects import mysql
from sqlalchemy import Integer, Column
from app import ma
# from flask_marshmallow import fields
from marshmallow import fields


class Tax(db.Model):
    __talename__ = 'tax'
    id = Column(mysql.BIGINT(unsigned=True),
                nullable=False, primary_key=True)
    user_id = Column(mysql.BIGINT(unsigned=True),
                     db.ForeignKey('user.id'), nullable=False)
    year = Column(Integer, nullable=False)