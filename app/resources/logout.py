from flask_restful import Resource
from flask_jwt_extended import get_raw_jwt, jwt_required, jwt_refresh_token_required
from app.models.revoked_token import RevokedTokenModel


class Logout_Access(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except Exception:
            return {'message': 'Something went wrong'}, 500


class Logout_Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except Exception:
            return {'message': 'Something went wrong'}, 500
