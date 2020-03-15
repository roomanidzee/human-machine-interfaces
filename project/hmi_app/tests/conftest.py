# -*- coding: utf-8 -*-

import pytest

from server import create_app
from server.config.dev import DevelopmentConfig
from server.config.prod import ProductionConfig, TestConfig

@pytest.fixture
def dev_app():
    return create_app(DevelopmentConfig)

@pytest.fixture
def test_app():
    return create_app(TestConfig)

@pytest.fixture
def prod_app():
    return create_app(ProductionConfig)

@pytest.fixture
def app_client(test_app):
    return test_app.test_client()
