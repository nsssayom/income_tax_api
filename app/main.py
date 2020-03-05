from flask_restful import Api
from app import app
from .resources.hello import Hello
from .resources.register import Register, Validate_Email, Validate_Phone
from .resources.login import Login
from .resources.auth import Auth
from .resources.token_refresh import Token_Refresh
from .resources.logout import Logout_Access, Logout_Refresh
from .resources.personal_info import Personal_Info
from .resources.income_info import Income_Info
from .resources.investment_info import Investment_Info
from .resources.tax_info import Tax_Info

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
api.add_resource(Income_Info, '/user/income_info')
api.add_resource(Investment_Info, '/user/investment_info')
api.add_resource(Tax_Info, '/user/tax_info')

if __name__ == "__main__":
    app.run(debug=True)
