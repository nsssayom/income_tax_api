from flask_restful import Api
from app import app
from .resources.hello import Hello
from .resources.register import Register
from .resources.login import Login
from .resources.auth import Auth
from .resources.token_refresh import Token_Refresh
from .resources.logout import Logout_Access

api = Api(app)

# routes
api.add_resource(Hello, '/hello')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Auth, '/auth')
api.add_resource(Token_Refresh, '/auth/refresh')
api.add_resource(Logout_Access, '/auth/logout')


if __name__ == "__main__":
    app.run(debug=True)
