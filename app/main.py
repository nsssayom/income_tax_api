from flask_restful import Api
from app import app
from .resources.hello import Hello
from .resources.register import Register, Validate_Email, Validate_Phone
from .resources.login import Login
from .resources.auth import Auth
from .resources.token_refresh import Token_Refresh
from .resources.logout import Logout_Access, Logout_Refresh
from .resources.personal_info import Personal_Info


api = Api(app)

# routes
api.add_resource(Hello, '/hello')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Auth, '/auth')
api.add_resource(Token_Refresh, '/auth/refresh')
api.add_resource(Logout_Access, '/logout')
api.add_resource(Logout_Refresh, '/logout/refresh')
api.add_resource(Validate_Email, '/validate/email')
api.add_resource(Validate_Phone, '/validate/phone')
api.add_resource(Personal_Info, '/user/info')

if __name__ == "__main__":
    app.run(debug=True)
