from flask_restful import Api
from app import app
from .resources.hello import Hello

api = Api(app)

# routes
api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(debug=True)
