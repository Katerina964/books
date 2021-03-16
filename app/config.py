import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://newssite:password@postgres:5432/newssite-database'
    FLASK_ADMIN_SWATCH = 'cerulean'

    SECURITY_URL_PREFIX = "/admin"
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"

    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = "/register/"
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
