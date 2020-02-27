from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User
from app import db
import re
import phonenumbers

rergister_parser = reqparse.RequestParser()
rergister_parser.add_argument(
    'username', type=str, help='Username cannot be blank', required=True)
rergister_parser.add_argument(
    'password', type=str, help='Password cannot be blank', required=True)
rergister_parser.add_argument(
    'email', type=str, help='email cannot be blank', required=True)
rergister_parser.add_argument(
    'phone', type=str, help='phone cannot be blank', required=True)

email_validation_parser = reqparse.RequestParser()
email_validation_parser.add_argument(
    'email', type=str, help='Email cannot be blank', required=True)

phone_validation_parser = reqparse.RequestParser()
phone_validation_parser.add_argument(
    'phone', type=str, help='Phone cannot be blank', required=True)


class Register(Resource):
    def post(self):
        data = rergister_parser.parse_args()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')

        # Email Validation
        if not Validate_Email.is_email_valid(email):
            return make_response(jsonify({
                'status': 400,
                'msg': "Invalid email address format"
            }), 400)

        if not Validate_Email.is_email_available(email):
            return make_response(jsonify({
                'status': 409,
                'msg': "Email address is already used"
            }), 409)

        # Phone Validation
        if not Validate_Phone.is_phone_valid(phone):
            return make_response(jsonify({
                'status': 400,
                'msg': "Invalid phone number"
            }), 400)
        
        if not Validate_Phone.is_phone_available(phone):
            return make_response(jsonify({
                'status': 409,
                'msg': "Phone number is already used"
            }), 409)

        try:
            user = User(name=username, email=email, phone=phone)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify({
                'status': 200,
                'msg': "Registration successful"
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 400,
                'msg': "Bad request"
            }), 400)


class Validate_Email(Resource):
    def post(set):
        data = email_validation_parser.parse_args()
        email = data.get('email')

        if not Validate_Email.is_email_valid(email):
            return make_response(jsonify({
                'status': 400,
                'msg': "Invalid email address format"
            }), 400)

        if not Validate_Email.is_email_available(email):
            return make_response(jsonify({
                'status': 409,
                'msg': "Email address is already used"
            }), 409)

        return make_response(jsonify({
                'status': 200,
                'msg': "Email address is valid and available"
            }), 200)

    @staticmethod
    def is_email_valid(email):
        if len(email) > 7:
            return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
        return False

    @staticmethod
    def is_email_available(email):
        current_user = User.find_by_email(email)
        if not current_user:
            return True
        return False


class Validate_Phone(Resource):
    def post(set):
        data = phone_validation_parser.parse_args()
        phone = data.get('phone')

        if not Validate_Phone.is_phone_valid(phone):
            return make_response(jsonify({
                'status': 400,
                'msg': "Invalid phone number"
            }), 400)
        
        if not Validate_Phone.is_phone_available(phone):
            return make_response(jsonify({
                'status': 409,
                'msg': "Phone number is already used"
            }), 409)

        return make_response(jsonify({
                'status': 200,
                'msg': "Phone number is valid and available"
            }), 200)

    @staticmethod
    def is_phone_valid(phone):
        num = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(num)

    @staticmethod
    def is_phone_available(phone):
        try:
            current_user = User.find_by_phone(phone)
            if not current_user:
                return True
            else:
                return False
        except Exception:
            return False
