# -*- coding: utf-8 -*-

import pytest

from server import create_app
from server.config.dev import DevelopmentConfig
from server.config.prod import ProductionConfig

@pytest.fixture
def dev_app():
    return create_app(DevelopmentConfig)

@pytest.fixture
def prod_app():
    return create_app(ProductionConfig)

@pytest.fixture
def app_client(dev_app):
    return dev_app.test_client()
