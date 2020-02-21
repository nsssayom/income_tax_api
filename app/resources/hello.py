from flask_restful import Resource
from app.models.user import User


class Hello(Resource):
    def get(self):
        User("1969")
        return {'Hello': 'World'}
