import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_redis import FlaskRedis
from dynaconf import FlaskDynaconf

from server.settings import (
    redis,
    logging
)

os.environ.setdefault('FLASK_ENV', 'development')


def create_app():
    """Function for initializing Flask application."""

    app = Flask(__name__)

    FlaskDynaconf(
        app,
        SETTINGS_FILE_FOR_DYNACONF="config.yml"
    )

    redis.configure(app)

    base_path = os.path.dirname(os.path.abspath(__file__))
    logging.configure(base_path)

    from server.modules.home.views import index
    from server.modules.numbers.views import numbers

    app.register_blueprint(index)
    app.register_blueprint(numbers)

    return app
