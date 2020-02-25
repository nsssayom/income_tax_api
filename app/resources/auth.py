from flask_restful import Resource  # , request, abort
# from app.models.user_test import User_Test
# from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import jwt


class Auth(Resource):
    @jwt_required
    @jwt.token_in_blacklist_loader
    def get(self):
        current_user = get_jwt_identity()
        return current_user
