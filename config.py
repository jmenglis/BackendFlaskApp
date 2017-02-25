import os, jinja2
import secrets

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = secrets.csrf_token

SECRET_KEY = secrets.secret_key