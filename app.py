from flask import Flask, Blueprint
from flask_restful import Api
from resources.Hello import Hello

# initilize app and Api
app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Hello, '/hello')


# Run app
if __name__ == '__main__':
    app.run()