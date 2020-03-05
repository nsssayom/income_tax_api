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

    # tax
    collected_at_source = Column(Integer, default=0)
    advance_paid = Column(Integer, default=0)
    adjustment = Column(Integer, default=0)
    total_tax = Column(Integer, default=0)

    def __init__(self, user_id, year):
        self.user_id = user_id,
        self.year = year

    @classmethod
    def find_by_userid(cls, userid, year):
        return cls.query.filter_by(user_id=userid).filter_by(year=year).first()

    def get_total_tax(self):
        tax = [self.collected_at_source, self.advance_paid,
               self.adjustment, self.total_tax]
        return sum(filter(None, tax))


class TaxSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Tax

    # Tax Schema
    collected_at_source = ma.auto_field()
    advance_paid = ma.auto_field()
    adjustment = ma.auto_field()
    total_tax = fields.Method("get_total_tax")

    def get_total_tax(self, obj):
        return obj.get_total_tax()
