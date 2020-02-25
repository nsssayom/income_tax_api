from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.user_test import User_Test
from app import db

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank',
                    required=True)
parser.add_argument('password', help='This field cannot be blank',
                    required=True)


class Register(Resource):
    def post(self):
        data = parser.parse_args()
        username = data.get('username')
        password = data.get('password')

        try:
            user = User_Test(name=username)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify('200 Success', {'data': {'username': username, 'password': password}}, {'code': 201})
        except Exception:
            return jsonify('400 Bad Request', {'code': 400})
