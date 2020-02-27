from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.models.user import User
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
import datetime


parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank',
                    required=True)
parser.add_argument('password', help='This field cannot be blank',
                    required=True)


class Login(Resource):
    def post(self):
        data = parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        current_user = User.find_by_email(email)

        if not current_user:
            return make_response(jsonify({
                'status': 404,
                'msg': "No account is associated with {}".format(email)
            }), 404)

        if User.verify_password(password, current_user.password_hash):
            expires = datetime.timedelta(days=365)
            access_token = create_access_token(identity=email, expires_delta=expires)
            refresh_token = create_refresh_token(identity=email)
            ret = {'access_token': access_token, 'refresh_token': refresh_token}
            return make_response(jsonify({
                'status': 200,
                'data': ret,
                'msg': 'Login successful'
            }), 200)
        else:
            return make_response(jsonify({
                'status': 401,
                'data': ret,
                'msg': 'Unauthorized request'
            }), 401)
