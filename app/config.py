import os

base_dir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:password@localhost/'
database_name = 'eplannerapi'


class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3600
    EVENTS_AND_TICKETS_PER_PAGE = 4
    SWAGGER_URL = '/docs'
    SWAGGER_API_URL = "http://172.17.242.17/ePlanner.yaml"


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base + database_name)
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 1
    AUTH_TOKEN_EXPIRY_SECONDS = 20
    EVENTS_AND_TICKETS_PER_PAGE = 4
    SWAGGER_URL = '/docs'
    SWAGGER_API_URL = "http://172.17.242.17/ePlanner.yaml"

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', postgres_local_base + database_name + "_test")
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECONDS = 3
    AUTH_TOKEN_EXPIRATION_TIME_DURING_TESTS = 5
    EVENTS_AND_TICKETS_PER_PAGE = 4