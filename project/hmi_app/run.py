import os

from server import create_app

from server.config.dev import DevelopmentConfig
from server.config.prod import ProductionConfig

if os.environ['FLASK_ENV'] == 'development':
    config_class = DevelopmentConfig
elif os.environ['FLASK_ENV'] == 'production':
    config_class = ProductionConfig

app = create_app(config_class)

if __name__ == '__main__':
    app.run(
        host=app.config['APP_HOST'],
        port=app.config['APP_PORT'],
        debug=app.config['FLASK_DEBUG'],
    )
