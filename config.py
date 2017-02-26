import os, jinja2
import secrets

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = secrets.csrf_token

SECRET_KEY = secrets.secret_key

TEMPLATE_FOLDER = "templates"

JINJA_ENVIRONMENT = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader([x[0] for x in os.walk('templates')])
])

ASSETS_FOLDER = "public"

# MONGODB SETUP
MONGO_HOST='localhost'
MONGO_PORT=27017
MONGO_DBNAME='FlaskTest'