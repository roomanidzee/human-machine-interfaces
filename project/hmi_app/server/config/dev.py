# -*- coding: utf-8 -*-

from pathlib import Path


class DevelopmentConfig(object):
    """Development configuration for system."""
    SECRET_KEY = 'nvo;zeivlno;zeihjnvf;osidjv;osdjmv;sldknvmcx'
    FLASK_DEBUG = 1
    BASE_PATH = Path(__file__).parent.parent.parent
    REDIS_URL = 'redis://localhost:6379/0'
    APP_HOST = 'localhost'
    APP_PORT = 5000
