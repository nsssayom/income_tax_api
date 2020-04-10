import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:978653@localhost/income_tax'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "HELLO WORLD!!!!".encode('utf8')
    JWT_SECRET_KEY = "HELLO WORLD!!!!"
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    DEBUG = 1
    ENV = 'development'
    CORS_ENABLED = True
    # Client ID:
    # 529739908096-rf6ql6jqh5brljolnvc4b232m4sdt2dp.apps.googleusercontent.com
    # Client Secret:
    # iyi0gXPhmWnx4kGtZ4C6VYKT
