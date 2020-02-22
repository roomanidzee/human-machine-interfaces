# -*- coding: utf-8 -*-

import pytest

from fakeredis import FakeRedis
from flask_redis import FlaskRedis

from server import create_app
from server.config.dev import DevelopmentConfig
from server.config.prod import ProductionConfig

def init_redis(app):
    """Configure redis for tests."""
    redis_store = FlaskRedis.from_custom_provider(FakeRedis)
    redis_store.init_app(app)

@pytest.fixture
def dev_app():
    app = create_app(DevelopmentConfig)
    init_redis(app)

    return app

@pytest.fixture
def prod_app():
    app = create_app(ProductionConfig)
    init_redis(app)

    return app
