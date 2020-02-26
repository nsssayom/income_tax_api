from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.user import User
from app import db
import re

rergister_parser = reqparse.RequestParser()
rergister_parser.add_argument('username', type=str, help='Username cannot be blank', required=True)
rergister_parser.add_argument('password', type=str, help='Password cannot be blank', required=True)
rergister_parser.add_argument('email', type=str, help='email cannot be blank', required=True)
rergister_parser.add_argument('phone', type=str, help='phone cannot be blank', required=True)

email_validation_parser = reqparse.RequestParser()
email_validation_parser.add_argument('email', type=str, help='Email cannot be blank', required=True)

phone_validation_parser = reqparse.RequestParser()
phone_validation_parser.add_argument('phone', type=str, help='Phone cannot be blank', required=True)


class Register(Resource):
    def post(self):
        data = rergister_parser.parse_args()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')

        if not Validate_Email.is_email_valid(email):
            return jsonify('409 Conflict', {'code': 409})

        try:
            user = User(name=username, email=email, phone=phone)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify('200 Success', {'data': {'username': username, 'password': password}}, {'code': 201})
        except Exception:
            return jsonify('400 Bad Request', {'code': 400})


class Validate_Email(Resource):
    def post(set):
        data = email_validation_parser.parse_args()
        email = data.get('email')

        if Validate_Email.is_email_valid(email):
            if Validate_Email.is_email_available(email):
                return jsonify('200 Success', {'data': {'email': email}}, {'code': 200})
            else:
                return jsonify('409 Conflict', {'code': 409})
        else:
            return jsonify('400 Bad Request', {'code': 400})

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
