from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User, UserSchema
from app.models.tax import Tax, TaxSchema
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

parser.add_argument('collected_at_source', type=int, required=False)
parser.add_argument('advance_paid', type=int, required=False)
parser.add_argument('adjustment', type=int, required=False)
parser.add_argument('total_tax', type=int, required=False)

get_parser = reqparse.RequestParser()
get_parser.add_argument('year', type=int, required=True,
                        help="Year cannot be empty")


class Tax_Info(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user = User.find_by_email(current_user)
        data = parser.parse_args()
        tax_info = Tax.find_by_userid(userid=user.id,
                                      year=data.get('year'))
        if tax_info is None:
            tax_info = Tax(user_id=user.id,
                           year=data.get('year'))
            db.session.add(tax_info)
            db.session.commit()
        try:
            tax_info.collected_at_source = data.get('collected_at_source')
            tax_info.advance_paid = data.get('advance_paid')
            tax_info.adjustment = data.get('adjustment')
            tax_info.total_tax = data.get('total_tax')

            db.session.commit()

            return make_response(jsonify({
                'status': 200,
                'msg': "Tax Information Updated"
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
        tax_info = Tax.find_by_userid(userid=user.id,
                                      year=data_.get('year'))
        try:
            tax_schema = TaxSchema()
            data = tax_schema.dump(tax_info)
            return make_response(jsonify({
                'status': 200,
                'data': data,
                'msg': "Tax Information"
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': "Internal server error"
            }), 500)        