from flask_restful import Resource  # , request, abort
# from app.models.user_test import User_Test
# from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import jwt
from flask import jsonify, make_response

class Auth(Resource):
    @jwt_required
    def post(self):
        return make_response(jsonify({
                'status': 200,
                'msg': 'Token Verified'
            }), 200)
