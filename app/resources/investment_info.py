from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User, UserSchema
from app.models.investment import Investment, InvestmentSchema
from app import db
import datetime
import json
import marshmallow
# import re
# import phonenumbers
from flask_jwt_extended import jwt_required, get_jwt_identity

parser = reqparse.RequestParser()

parser.add_argument('year', type=int, required=True,
                    help="Year cannot be empty")

parser.add_argument('life_insurance', type=int, required=False, store_missing=False)
parser.add_argument('deferred_contrib', type=int, required=False, store_missing=False)
parser.add_argument('provident_contrib', type=int, required=False, store_missing=False)
parser.add_argument('employers_provident_contrib', type=int, required=False, store_missing=False)
parser.add_argument('super_annuation_contrib', type=int, required=False, store_missing=False)
parser.add_argument('debenture_invest', type=int, required=False, store_missing=False)
parser.add_argument('deposit_pension_contrib', type=int, required=False, store_missing=False)
parser.add_argument('benevolent_fund_contrib', type=int, required=False, store_missing=False)
parser.add_argument('zakat_fund_contrib', type=int, required=False, store_missing=False)
parser.add_argument('other_investment_detail', type=str, required=False, store_missing=False)
parser.add_argument('other_investment', type=int, required=False, store_missing=False)

get_parser = reqparse.RequestParser()
get_parser.add_argument('year', type=int, required=True,
                        help="Year cannot be empty")


class Investment_Info(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user = User.find_by_email(current_user)
        data = parser.parse_args()
        investment_info = Investment.find_by_userid(userid=user.id,
                                                    year=data.get('year'))
        if investment_info is None:
            investment_info = Investment(user_id=user.id,
                                         year=data.get('year'))
            db.session.add(investment_info)
            db.session.commit()
        try:
            if 'life_insurance' in data:
                investment_info.life_insurance = data.get('life_insurance')
            if 'deferred_contrib' in data:
                investment_info.deferred_contrib = data.get('deferred_contrib')
            if 'provident_contrib' in data:
                investment_info.provident_contrib = data.get('provident_contrib')
            if 'employers_provident_contrib' in data:
                investment_info.employers_provident_contrib = data.get(
                'employers_provident_contrib')
            if 'super_annuation_contrib' in data:
                investment_info.super_annuation_contrib = data.get(
                'super_annuation_contrib')
            if 'debenture_invest' in data:    
                investment_info.debenture_invest = data.get('debenture_invest')
            if 'deposit_pension_contrib' in data:
                investment_info.deposit_pension_contrib = data.get(
                'deposit_pension_contrib')
            if 'benevolent_fund_contrib' in data:
                investment_info.benevolent_fund_contrib = data.get(
                'benevolent_fund_contrib')
            if 'zakat_fund_contrib' in data:
                investment_info.zakat_fund_contrib = data.get('zakat_fund_contrib')
            if 'other_investment_detail' in data:
                investment_info.other_investment_detail = data.get(
                'other_investment_detail')
            if 'other_investment' in data:
                investment_info.other_investment = data.get('other_investment')
            db.session.commit()

            return make_response(jsonify({
                'status': 200,
                'msg': "Investment Information Updated"
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
        investment_info = Investment.find_by_userid(userid=user.id,
                                                    year=data_.get('year'))
        try:
            investment_schema = InvestmentSchema()
            data = investment_schema.dump(investment_info)
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
