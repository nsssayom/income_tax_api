import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:97865321@localhost/income_tax'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
