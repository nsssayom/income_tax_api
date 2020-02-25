from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.user_test import User_Test
from app import db
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank',
                    required=True)
parser.add_argument('password', help='This field cannot be blank',
                    required=True)


class Login(Resource):
    def post(self):
        data = parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        current_user = User_Test.find_by_username(username)

        if not current_user:
            return jsonify('400 Bad Request', {'code': 400})

        if User_Test.verify_password(password, current_user.password_hash):
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return jsonify('200 Success', {'data': {'username': username, 'access-token': access_token, 'refresh-token': refresh_token}}, {'code': 200})
        else:
            return jsonify('401 Unautrorized', {'code': 401})
