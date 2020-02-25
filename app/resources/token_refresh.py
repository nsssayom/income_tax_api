from flask_restful import Resource
from app import jwt
# , request, abort
# from app.models.user_test import User_Test
# from app import db
from flask_jwt_extended import jwt_refresh_token_required, \
    get_jwt_identity, create_access_token


class Token_Refresh(Resource):
    @jwt_refresh_token_required
    @jwt.token_in_blacklist_loader
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return access_token
