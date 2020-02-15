# -*- coding: utf-8 -*-
import os
from typing import Dict, Set

from flask import current_app

class RedisService:
    """Service for working with Redis."""

    def __init__(self):
        self.redis_client = current_app.extensions['redis_client']

    def save_dict(input: Dict[int, str]) -> None:
        """Save ids and file_paths to redis."""

        for key, value in input.items():
            self.redis_client.set(str(key), value)

    def validate_for_keys(input: Set[str]) -> bool:
        """Validate, if all input keys exists."""

        keys = set(self.redis_client.scan_iter())

        diff = keys - modified_input

        return not bool(diff)

