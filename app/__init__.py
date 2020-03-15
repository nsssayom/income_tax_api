from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app, resources={r"*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
jwt = JWTManager(app)
ma = Marshmallow(app)

from app import main, models