from pathlib import Path

from flask import Flask
from flask_redis import FlaskRedis

from server.settings import (
    logging
)

base_path = Path(__file__).parent.parent
redis_client = FlaskRedis()

def register_extensions(app):
    """Method for register Flask extensions."""
    redis_client.init_app(app)
    logging.configure(base_path)

def register_endpoints(app):
    """Method for register Flask endpoints."""
    from server.modules.home.views import index
    from server.modules.numbers.views import numbers

    app.register_blueprint(index)
    app.register_blueprint(numbers)


def create_app(config_class):
    """Method for initialization of full system."""

    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_endpoints(app)        

    return app