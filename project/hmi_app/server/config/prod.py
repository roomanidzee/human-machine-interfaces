# -*- coding: utf-8 -*-

from pathlib import Path

class ProductionConfig(object):
    """Production configuration for system."""
    SECRET_KEY = 'nvo;zeivlno;zeihjnvf;osidjv;osdjmv;sldknvmcx'
    FLASK_DEBUG = 0
    BASE_PATH = Path(__file__).parent.parent / Path('logs')
    REDIS_URL = 'redis://redis_server:6379/0'
    APP_HOST = 'app'
    APP_PORT = 6500