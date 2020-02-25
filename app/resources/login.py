from flask_restful import Resource, request, abort
from app.models.user_test import User_Test
from app import db


class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if username is None or password is None:
            abort(400)
        if User_Test.query.filter_by(name=username).first() is not None:
            return "Error"
        user = User_Test(name=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return username
