from app import db
from sqlalchemy.dialects import mysql
from sqlalchemy import Integer, Column
from app import ma
# from flask_marshmallow import fields
from marshmallow import fields


class Income(db.Model):
    __tablename__ = 'income'
    id = Column(mysql.BIGINT(unsigned=True),
                nullable=False, primary_key=True)
    user_id = Column(mysql.BIGINT(unsigned=True),
                     db.ForeignKey('user.id'), nullable=False)
    year = Column(Integer, nullable=False)

    # Salary incomes
    basic = Column(Integer, default=0)
    special = Column(Integer, server_default="0")
    dearness = Column(Integer, default=0)
    conveyance = Column(Integer, default=0)
    house_rent = Column(Integer, default=0)
    medical = Column(Integer, default=0)
    servant = Column(Integer, default=0)
    leave = Column(Integer, default=0)
    honorarium = Column(Integer, default=0)
    over_time = Column(Integer, default=0)
    bonus = Column(Integer, default=0)
    other_allowances = Column(Integer, default=0)
    provident_fund_contrib = Column(Integer, default=0)
    provident_fund_interest = Column(Integer, default=0)
    deemed_transport = Column(Integer, default=0)
    deemed_accomodation_type = Column(mysql.BOOLEAN, default=False)
    deemed_accomodation = Column(Integer, default=0)
    other_income_detail = Column(mysql.VARCHAR(255), nullable=True)
    other_income = Column(Integer, default=0)

    # Other incomes
    interest_on_securities = Column(Integer, default=0)
    agricultural_income = Column(Integer, default=0)
    capital_gains = Column(Integer, default=0)

    # House incomes
    property_description = Column(mysql.VARCHAR(512), nullable=True)
    annual_rental_income = Column(Integer, default=0)
    # House expenses
    repair_expense = Column(Integer, default=0)
    municipal_tax = Column(Integer, default=0)
    land_revenue = Column(Integer, default=0)
    interest_on_loan = Column(Integer, default=0)
    insurance_premium = Column(Integer, default=0)
    vacancy_allowance = Column(Integer, default=0)
    other_expense = Column(Integer, default=0)

    def __init__(self, user_id, year):
        self.user_id = user_id,
        self.year = year

    @classmethod
    def find_by_userid(cls, userid, year):
        return cls.query.filter_by(user_id=userid).filter_by(year=year).first()

    def get_total_salary_income(self):
        incomes = [self.basic, self.special, self.dearness, self.conveyance,
                   self.house_rent, self.medical, self.servant, self.leave,
                   self.honorarium, self.over_time, self.bonus,
                   self.provident_fund_contrib, self.provident_fund_interest,
                   self.deemed_transport, self.deemed_accomodation_type,
                   self.deemed_accomodation, self.other_income_detail,
                   self.other_income, self.other_allowances]
        return sum(filter(None, incomes))

    def get_total_other_income(self):
        other_incomes = [self.interest_on_securities,
                         self.agricultural_income,
                         self.capital_gains]
        return (sum(filter(None, other_incomes)))

    def get_net_salary_income(self):
        net_incomes = [self.get_total_salary_income(),
                       self.get_total_other_income()]
        return (sum(filter(None, net_incomes)))

    def get_total_house_expense(self):
        house_expense = [self.repair_expense,
                         self.municipal_tax,
                         self.land_revenue,
                         self.interest_on_loan,
                         self.insurance_premium,
                         self.vacancy_allowance,
                         self.other_expense]
        return (sum(filter(None, house_expense)))

    def get_net_house_income(self):
        if (self.annual_rental_income == 0) or \
           (self.annual_rental_income is None):
            return 0
        else:
            return (self.annual_rental_income - self.get_total_house_expense())

    # Methods for Schedule-1(Salaries)
    def get_exempted_income(self):
        exempted = {}
        exempted["basic"] = 0
        exempted["special"] = 0
        exempted["dearness"] = 0
        exempted["conveyance"] = 30000
        exempted["house_rent"] = min([int(self.basic * 0.5), 25000*12])
        if (self.user.is_disable):
            exempted["medical"] = min([int(self.basic * 0.1), 1000000])
        else:
            exempted["medical"] = min([int(self.basic * 0.1), 120000])
        exempted["servant"] = 0,
        exempted["leave"] = 0
        exempted["honorarium"] = 0
        exempted["over_time"] = 0
        exempted["bonus"] = 0
        exempted["provident_fund_contrib"] = 0
        exempted["provident_fund_interest"] = min([int((self.basic +
                                                        self.dearness) *
                                                       (1/3)), 120000])  # TODO: Add another elelment
        exempted["deemed_transport"] = 0
        exempted["deemed_accomodation"] = 0
        exempted["other_income_detail"] = 0
        exempted["other_income"] = 0
        exempted["other_allowances"] = 0
        
        return exempted


class OtherIncomeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Income

    # Other incomes
    interest_on_securities = ma.auto_field()
    agricultural_income = ma.auto_field()
    capital_gains = ma.auto_field()
    total_other_income = fields.Method("get_total_other_income")

    def get_total_other_income(self, obj):
        return obj.get_total_other_income()


class SalaryIncomeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Income

        # Salary incomes
    basic = ma.auto_field()
    special = ma.auto_field()
    dearness = ma.auto_field()
    conveyance = ma.auto_field()
    house_rent = ma.auto_field()
    medical = ma.auto_field()
    servant = ma.auto_field()
    leave = ma.auto_field()
    honorarium = ma.auto_field()
    over_time = ma.auto_field()
    bonus = ma.auto_field()
    other_allowances = ma.auto_field()
    provident_fund_contrib = ma.auto_field()
    provident_fund_interest = ma.auto_field()
    deemed_transport = ma.auto_field()
    deemed_accomodation_type = ma.auto_field()
    deemed_accomodation = ma.auto_field()
    other_income_detail = ma.auto_field()
    other_income = ma.auto_field()
    total_salary_income = fields.Method("get_total_salary_income")

    def get_total_salary_income(self, obj):
        return obj.get_total_salary_income()


class IncomeSchema(ma.SQLAlchemySchema):
    net_salary_income = fields.Method("get_net_salary_income")

    def get_net_salary_income(self, obj):
        return obj.get_net_salary_income()


class HouseExpenseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Income
    # House expenses
    repair_expense = ma.auto_field()
    municipal_tax = ma.auto_field()
    land_revenue = ma.auto_field()
    interest_on_loan = ma.auto_field()
    insurance_premium = ma.auto_field()
    vacancy_allowance = ma.auto_field()
    other_expense = ma.auto_field()
    total_house_expense = fields.Method("get_total_house_expense")

    def get_total_house_expense(self, obj):
        return obj.get_total_house_expense()


class HouseIncomeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Income

    # House incomes
    property_description = ma.auto_field()
    annual_rental_income = ma.auto_field()
    net_house_income = fields.Method("get_net_house_income")

    def get_net_house_income(self, obj):
        return obj.get_net_house_income()
