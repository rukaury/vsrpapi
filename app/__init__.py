import os
from flask import Flask
from flask_bcrypt import Bcrypt

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Register blueprints
from app.auth.views import auth

app.register_blueprint(auth, url_prefix='/v1')

from app.programs.views import programs

app.register_blueprint(programs, url_prefix='/v1')

# Import the application views
from app import views
