import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_redis import FlaskRedis
from dynaconf import FlaskDynaconf

os.environ.setdefault('FLASK_ENV', 'development')


def create_app():
    """Function for initializing Flask application."""

    app = Flask(__name__)

    FlaskDynaconf(
        app,
        SETTINGS_FILE_FOR_DYNACONF="config.yml"
    )

    redis_client = FlaskRedis()
    redis_client.init_app(app)
    
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(
        base_path,
        app.config.logs.directory,
    )
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    logging.basicConfig(
        level=logging.INFO,
        format=app.config.logs.format,
        handlers=[
            TimedRotatingFileHandler(
                filename=f"{log_path}/hmi_app.({current_time}).log",
                encoding='utf-8',
                when="d",
                backupCount=5,
                interval=1
            ),
            logging.StreamHandler()
        ]
    )
    """

    return app
