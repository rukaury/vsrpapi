import os
from neomodel import config as neoconfig 

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3600
    ITEMS_PER_PAGE = 4


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 1
    AUTH_TOKEN_EXPIRY_SECONDS = 20
    ITEMS_PER_PAGE = 4
    neoconfig.DATABASE_URL = os.environ["NEO4J_BOLT_URL"]

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECONDS = 3
    AUTH_TOKEN_EXPIRATION_TIME_DURING_TESTS = 5
    ITEMS_PER_PAGE = 4