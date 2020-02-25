from flask_restful import Api
from app import app
from .resources.hello import Hello
from .resources.register import Register


api = Api(app)

# routes
api.add_resource(Hello, '/hello')
api.add_resource(Register, '/register')

if __name__ == "__main__":
    app.run(debug=True)
