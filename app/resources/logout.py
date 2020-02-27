from flask_restful import Resource
from flask import jsonify, make_response
from flask_jwt_extended import get_raw_jwt, jwt_required, jwt_refresh_token_required
from app.models.revoked_token import RevokedTokenModel
from app import jwt 

class Logout_Access(Resource):
    @jwt_required
    @jwt.expired_token_loader
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return make_response(jsonify({
                'status': 200,
                'msg': 'Access_Logout successful'
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': 'Internal Server Error'
            }), 500)


class Logout_Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return make_response(jsonify({
                'status': 200,
                'msg': 'Refresh_Logout successful'
            }), 200)
        except Exception:
            return make_response(jsonify({
                'status': 500,
                'msg': 'Internal Server Error'
            }), 500)
