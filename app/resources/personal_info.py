from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User, UserSchema
from app import db
import datetime
import json
# import re
# import phonenumbers
from flask_jwt_extended import jwt_required, get_jwt_identity

parser = reqparse.RequestParser()
parser.add_argument(
    'dob', help='Date of Birth cannot be blank', required=False)
parser.add_argument(
    'gender', choices=('male', 'female'), help='Bad Choice for gender', required=False)
parser.add_argument(
    'address', type=str, help='Address cannot be blank', required=False)
parser.add_argument(
    'is_ff', type=bool, choices=(True, False), required=False)
parser.add_argument(
    'is_disable', type=bool, choices=(True, False), required=False)
parser.add_argument(
    'is_parent_disable', type=bool, choices=(True, False), required=False)


class Personal_Info(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user = User.find_by_email(current_user)
        data = parser.parse_args()
        try:
            # user.dob = data.get('dob')
            user.gender = data.get('gender')
            user.address = data.get('address')
            user.is_ff = data.get('is_ff')
            user.is_disable = data.get('is_disable')
            user.is_parent_disable = data.get('is_parent_disable')

            dob = data.get('dob')
            json_dob = dob.replace("'", "\"")
            dob_ = json.loads(json_dob)

            user.dob = datetime.date(dob_['year'], dob_['month'], dob_['day'])

            db.session.commit()

            return make_response(jsonify({
                'status': 200,
                'msg': "Personal Information Updated"
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
        try:
            info_schema = UserSchema()
            data = info_schema.dump(user)
            return make_response(jsonify({
                'status': 200,
                'data': data,
                'msg': "Personal Information Updated"
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': "Internal server error"
            }), 500)

