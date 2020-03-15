# -*- coding: utf-8 -*-

from pathlib import Path

class ProductionConfig(object):
    """Production configuration for system."""
    
    SECRET_KEY = 'nvo;zeivlno;zeihjnvf;osidjv;osdjmv;sldknvmcx'

    FLASK_DEBUG = 0

    BASE_PATH = Path(__file__).parent.parent / Path('logs')

    REDIS_URL = 'redis://redis:6379/0'

    APP_HOST = '0.0.0.0'
    APP_PORT = 6500

class TestConfig(ProductionConfig):
    """System configuration for tests"""
    FLASK_DEBUG = 1