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

    log_fmt = '%(asctime)s [%(threadName)-12.12s] [%(levelname)-7s] %(message)s'

    logging.basicConfig(
        level=logging.INFO,
        format=log_fmt,
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
