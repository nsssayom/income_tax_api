from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User, UserSchema
from app.models.income import Income, SalaryIncomeSchema, OtherIncomeSchema, \
                              IncomeSchema, HouseExpenseSchema, \
                              HouseIncomeSchema
from app import db
import datetime
import json
import marshmallow
# import re
# import phonenumbers
from flask_jwt_extended import jwt_required, get_jwt_identity

parser = reqparse.RequestParser()

parser.add_argument('year', type=int, required=True, help="Year cannot be empty")

parser.add_argument('basic', type=int, required=False)
parser.add_argument('special', type=int, required=False)
parser.add_argument('dearness', type=int, required=False)
parser.add_argument('conveyance', type=int, required=False)
parser.add_argument('house_rent', type=int, required=False)
parser.add_argument('medical', type=int, required=False)
parser.add_argument('servant', type=int, required=False)
parser.add_argument('leave', type=int, required=False)
parser.add_argument('honorarium', type=int, required=False)
parser.add_argument('over_time', type=int, required=False)
parser.add_argument('bonus', type=int, required=False)
parser.add_argument('other_allowances', type=int, required=False)
parser.add_argument('provident_fund_contrib', type=int, required=False)
parser.add_argument('provident_fund_interest', type=int, required=False)
parser.add_argument('deemed_transport', type=int, required=False)
parser.add_argument('deemed_accomodation_type', type=bool, required=False)
parser.add_argument('deemed_accomodation', type=int, required=False)
parser.add_argument('other_income_detail', type=str, required=False)
parser.add_argument('other_income', type=int, required=False)
parser.add_argument('interest_on_securities', type=int, required=False)
parser.add_argument('agricultural_income', type=int, required=False)
parser.add_argument('capital_gains', type=int, required=False)

parser.add_argument('annual_rental_income', type=int, required=False)
parser.add_argument('repair_expense', type=int, required=False)
parser.add_argument('municipal_tax', type=int, required=False)
parser.add_argument('land_revenue', type=int, required=False)
parser.add_argument('interest_on_loan', type=int, required=False)
parser.add_argument('insurance_premium', type=int, required=False)
parser.add_argument('vacancy_allowance', type=int, required=False)
parser.add_argument('other_expense', type=int, required=False)

get_parser = reqparse.RequestParser()
get_parser.add_argument('year', type=int, required=True, help="Year cannot be empty")


class Income_Info(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user = User.find_by_email(current_user)
        data = parser.parse_args()
        income_info = Income.find_by_userid(userid=user.id, 
                                            year=data.get('year'))
        if income_info is None:
            income_info = Income(user_id=user.id,
                                 year=data.get('year'))
            db.session.add(income_info)
            db.session.commit()
        try:
            income_info.basic = data.get('basic')
            income_info.special = data.get('special')
            income_info.dearness = data.get('dearness')
            income_info.conveyance = data.get('conveyance')
            income_info.house_rent = data.get('house_rent')
            income_info.medical = data.get('medical')
            income_info.servant = data.get('servant')
            income_info.leave = data.get('leave')
            income_info.honorarium = data.get('honorarium')
            income_info.over_time = data.get('over_time')
            income_info.bonus = data.get('bonus')
            income_info.other_allowances = data.get('other_allowances')
            income_info.provident_fund_contrib = data.get('provident_fund_contrib')
            income_info.provident_fund_interest = data.get('provident_fund_interest')
            income_info.deemed_transport = data.get('deemed_transport')
            income_info.deemed_accomodation_type = data.get('deemed_accomodation_type')
            income_info.deemed_accomodation = data.get('deemed_accomodation')
            income_info.other_income_detail = data.get('other_income_detail')
            income_info.other_income = data.get('other_income')
            income_info.interest_on_securities = data.get('interest_on_securities')
            income_info.agricultural_income = data.get('agricultural_income')
            income_info.capital_gains = data.get('capital_gains')

            income_info.annual_rental_income = data.get('annual_rental_income')
            income_info.repair_expense = data.get('repair_expense')
            income_info.municipal_tax = data.get('municipal_tax')
            income_info.land_revenue = data.get('land_revenue')
            income_info.interest_on_loan = data.get('interest_on_loan')
            income_info.insurance_premium = data.get('insurance_premium')
            income_info.vacancy_allowance = data.get('vacancy_allowance')
            income_info.other_expense = data.get('other_expense')

            db.session.commit()

            return make_response(jsonify({
                'status': 200,
                'msg': "Income Information Updated"
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': "Internal server error"
            }), 500)

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = User.find_by_email(current_user)
        data_ = get_parser.parse_args()
        income_Info = Income.find_by_userid(userid=user.id, 
                                            year=data_.get('year'))

        try:
            house_expense = HouseExpenseSchema()
            house_income = HouseIncomeSchema()
            salary_income = SalaryIncomeSchema()
            other_income = OtherIncomeSchema()
            income = IncomeSchema()

            income = income.dump(income_Info)
            income['salary_income'] = salary_income.dump(income_Info)
            income['other_income'] = other_income.dump(income_Info)

            house_income_ = house_income.dump(income_Info)
            house_income_['expense'] = house_expense.dump(income_Info)
            
            income['house_income'] = house_income_
            income

            data = {}
            data['income'] = income
            return make_response(jsonify({
                'status': 200,
                'data': data,
                'msg': "Income Information"
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': "Internal server error"
            }), 500)
