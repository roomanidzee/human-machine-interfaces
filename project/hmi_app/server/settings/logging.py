# -*- coding: utf-8 -*-

import os
import datetime
import logging

from logging.handlers import TimedRotatingFileHandler

def configure(base_path):
    """Configure logging for system."""

    log_path = os.path.join(
        base_path,
        'logs',
    )
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(threadName)-12.12s] [in %(pathname)s:%(lineno)d in %(funcName)s] [%(levelname)-5.5s]  %(message)s',
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
