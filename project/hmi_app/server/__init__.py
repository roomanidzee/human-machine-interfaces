import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from dynaconf import FlaskDynaconf
from redis import Redis

from server.settings import (
    logging
)

os.environ.setdefault('FLASK_ENV', 'development')
os.environ.setdefault('SETTINGS_MODULE_FOR_DYNACONF', 'config/settings.yml')

app = Flask(__name__)

FlaskDynaconf(app)

redis_client = Redis(
    host='localhost',
    port=6379,
    db=0
)

base_path = os.path.dirname(os.path.abspath(__file__))
logging.configure(base_path)

from server.modules.home.views import index
from server.modules.numbers.views import numbers

app.register_blueprint(index)
app.register_blueprint(numbers)

