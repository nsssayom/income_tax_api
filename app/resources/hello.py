from flask_restful import Resource
from app.models.user import User
from app import db


class Hello(Resource):
    def get(self):
        # user = User(name="Sreejan",
        #             email="sreejan@retriko.com", phone="+8801717018076")
        # user.hash_password("123456")
        # db.session.add(user)
        # db.session.commit()
        return {'msg': 'Stay Home, World'}
