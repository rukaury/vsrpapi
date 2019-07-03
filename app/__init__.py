import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# Initialize application
app = Flask(__name__, static_folder=None)

# Enabling cors
CORS(app)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.ProductionConfig'
)

app.config.from_object(app_settings)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Register blueprints
from app.auth.views import auth

app.register_blueprint(auth, url_prefix='/v1')

from app.programs.views import programs

app.register_blueprint(programs, url_prefix='/v1')

from app.schools.views import schools

app.register_blueprint(schools, url_prefix='/v1')

from app.courses.views import courses

app.register_blueprint(courses, url_prefix='/v1')

from app.room.views import rooms

app.register_blueprint(rooms, url_prefix='/v1')

from app.user.views import users

app.register_blueprint(users, url_prefix='/v1')


# Import the application views
from app import views
