from flask_restful import Resource
from flask import jsonify, make_response
from app import jwt
# , request, abort
# from app.models.user_test import User_Test
# from app import db
from flask_jwt_extended import jwt_refresh_token_required, \
    get_jwt_identity, create_access_token, create_refresh_token
import datetime


class Token_Refresh(Resource):
    @jwt_refresh_token_required
    @jwt.token_in_blacklist_loader
    def post(self):
        current_user = get_jwt_identity()
        expires = datetime.timedelta(days=365)
        access_token = create_access_token(identity=current_user, expires_delta=expires)
        refresh_token = create_refresh_token(identity=current_user)

        ret = {'access_token': access_token, 'refresh_token': refresh_token}
        return make_response(jsonify({
            'status': 200,
            'data': ret,
            'msg': 'Token refresh successful'
        }), 200)
