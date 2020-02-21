from flask_restful import Resource
from app.models.user import User


class Hello(Resource):
    def get(self):
        User("jamil")
        return {'Hello': 'World'}
