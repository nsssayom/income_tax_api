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

import traceback
import sys

parser = reqparse.RequestParser()

parser.add_argument('year', type=int, required=True, help="Year cannot be empty")

parser.add_argument('basic', type=int, store_missing=False, required=False)
parser.add_argument('special', type=int, store_missing=False, required=False)
parser.add_argument('dearness', type=int, store_missing=False, required=False)
parser.add_argument('conveyance', type=int, store_missing=False, required=False)
parser.add_argument('house_rent', type=int, store_missing=False, required=False)
parser.add_argument('medical', type=int, store_missing=False, required=False)
parser.add_argument('servant', type=int, store_missing=False, required=False)
parser.add_argument('leave', type=int, store_missing=False, required=False)
parser.add_argument('honorarium', type=int, store_missing=False, required=False)
parser.add_argument('over_time', type=int, store_missing=False, required=False)
parser.add_argument('bonus', type=int, store_missing=False, required=False)
parser.add_argument('other_allowances', type=int, store_missing=False, required=False)
parser.add_argument('provident_fund_contrib', type=int, store_missing=False, required=False)
parser.add_argument('provident_fund_interest', type=int, store_missing=False, required=False)
parser.add_argument('deemed_transport', type=int, store_missing=False, required=False)
parser.add_argument('deemed_accomodation_type', type=bool, store_missing=False, required=False)
parser.add_argument('deemed_accomodation', type=int, store_missing=False, required=False)
parser.add_argument('other_income_detail', type=str, store_missing=False, required=False)
parser.add_argument('other_income', type=int, store_missing=False, required=False)
parser.add_argument('interest_on_securities', type=int, store_missing=False, required=False)
parser.add_argument('agricultural_income', type=int, store_missing=False, required=False)
parser.add_argument('capital_gains', type=int, store_missing=False, required=False)

parser.add_argument('annual_rental_income', type=int, store_missing=False, required=False)
parser.add_argument('repair_expense', type=int, store_missing=False, required=False)
parser.add_argument('municipal_tax', type=int, store_missing=False, required=False)
parser.add_argument('land_revenue', type=int, store_missing=False, required=False)
parser.add_argument('interest_on_loan', type=int, store_missing=False, required=False)
parser.add_argument('insurance_premium', type=int, store_missing=False, required=False)
parser.add_argument('vacancy_allowance', type=int, store_missing=False, required=False)
parser.add_argument('other_expense', type=int, store_missing=False, required=False)

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
            if 'basic' in data:
                income_info.basic = data.get('basic')
            if 'special' in data:
                income_info.special = data.get('special')
            if 'dearness' in data:
                income_info.dearness = data.get('dearness')
            if 'conveyance' in data:
                income_info.conveyance = data.get('conveyance')
            if 'house_rent' in data:
                income_info.house_rent = data.get('house_rent')
            if 'medical' in data:
                income_info.medical = data.get('medical')
            if 'servant' in data:
                income_info.servant = data.get('servant')
            if 'leave' in data:
                income_info.leave = data.get('leave')
            if 'honorarium' in data:
                income_info.honorarium = data.get('honorarium')
            if 'over_time' in data:
                income_info.over_time = data.get('over_time')
            if 'bonus' in data:
                income_info.bonus = data.get('bonus')
            if 'other_allowances' in data:
                income_info.other_allowances = data.get('other_allowances')
            if 'provident_fund_contrib' in data:
                income_info.provident_fund_contrib = data.get('provident_fund_contrib')
            if 'provident_fund_interest' in data:
                income_info.provident_fund_interest = data.get('provident_fund_interest')
            if 'deemed_transport' in data:
                income_info.deemed_transport = data.get('deemed_transport')
            if 'deemed_accomodation_type' in data:
                income_info.deemed_accomodation_type = data.get('deemed_accomodation_type')
            if 'deemed_accomodation' in data:
                income_info.deemed_accomodation = data.get('deemed_accomodation')
            if 'other_income_detail' in data:
                income_info.other_income_detail = data.get('other_income_detail')
            if 'other_income' in data:
                income_info.other_income = data.get('other_income')
            if 'interest_on_securities' in data:
                income_info.interest_on_securities = data.get('interest_on_securities')
            if 'agricultural_income' in data:
                income_info.agricultural_income = data.get('agricultural_income')
            if 'capital_gains' in data:
                income_info.capital_gains = data.get('capital_gains')

            if 'annual_rental_income' in data:
                income_info.annual_rental_income = data.get('annual_rental_income')
            if 'repair_expense' in data:
                income_info.repair_expense = data.get('repair_expense')
            if 'municipal_tax' in data:
                income_info.municipal_tax = data.get('municipal_tax')
            if 'land_revenue' in data:
                income_info.land_revenue = data.get('land_revenue')
            if 'interest_on_loan' in data:
                income_info.interest_on_loan = data.get('interest_on_loan')
            if 'insurance_premium' in data:
                income_info.insurance_premium = data.get('insurance_premium')
            if 'vacancy_allowance' in data:
                income_info.vacancy_allowance = data.get('vacancy_allowance')
            if 'other_expense' in data:
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
        print(current_user)
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

            data = {}
            data['income'] = income
            
            return make_response(jsonify({
                'status': 200,
                'data': data,
                'msg': "Income Information"
            }), 200)
        except:
            return make_response(jsonify({
                'status': 500,
                'msg': traceback.format_exc()
                # or
                # print(sys.exc_info()[2])
            }), 500)
