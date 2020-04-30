from app import db
from sqlalchemy.dialects import mysql
from sqlalchemy import Integer, Column
from app import ma
# from flask_marshmallow import fields
from marshmallow import fields


class Investment(db.Model):
    __tablename__ = 'investment'
    id = Column(mysql.BIGINT(unsigned=True),
                nullable=False, primary_key=True)
    user_id = Column(mysql.BIGINT(unsigned=True),
                     db.ForeignKey('user.id'), nullable=False)
    year = Column(Integer, nullable=False)
    
    # investment
    life_insurance = Column(Integer, default=0)
    deferred_contrib = Column(Integer, default=0)
    provident_contrib = Column(Integer, default=0)
    employers_provident_contrib = Column(Integer, default=0)
    super_annuation_contrib = Column(Integer, default=0)
    debenture_invest = Column(Integer, default=0)
    deposit_pension_contrib = Column(Integer, default=0)
    benevolent_fund_contrib = Column(Integer, default=0)
    zakat_fund_contrib = Column(Integer, default=0)
    other_investment_detail = Column(mysql.VARCHAR(255), unique=False, nullable=True)
    other_investment = Column(Integer, default=0)

    def __init__(self, user_id, year):
        self.user_id = user_id,
        self.year = year

    @classmethod
    def find_by_userid(cls, userid, year):
        return cls.query.filter_by(user_id=userid).filter_by(year=year).first()

    def get_total_investment(self):

        investment = [self.life_insurance, self.deferred_contrib,
                      self.provident_contrib, self.employers_provident_contrib,
                      self.super_annuation_contrib, self.debenture_invest,
                      self.deposit_pension_contrib,
                      self.benevolent_fund_contrib,
                      self.zakat_fund_contrib, self.other_investment]
        return sum(filter(None, investment))


class InvestmentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Investment

    # Investment Schema
    life_insurance = ma.auto_field()
    deferred_contrib = ma.auto_field()
    provident_contrib = ma.auto_field()
    employers_provident_contrib = ma.auto_field()
    super_annuation_contrib = ma.auto_field()
    debenture_invest = ma.auto_field()
    deposit_pension_contrib = ma.auto_field()
    benevolent_fund_contrib = ma.auto_field()
    zakat_fund_contrib = ma.auto_field()
    other_investment_detail = ma.auto_field()
    other_investment = ma.auto_field()
    total_investment = fields.Method("get_total_investment")

    def get_total_investment(self, obj):
        return obj.get_total_investment()
