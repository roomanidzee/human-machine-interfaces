# -*- coding: utf-8 -*-
import os
from typing import Dict, Set

from server import redis_client

class RedisService:
    """Service for working with Redis."""

    def __init__(self):
        self.redis_client = redis_client

    def save_dict(self, input: Dict[int, str]) -> None:
        """Save ids and file_paths to redis."""

        for key, value in input.items():
            self.redis_client.set(str(key), value)

    def validate_for_keys(self, elem_input: Set[str]) -> Set[str]:
        """Validate, if all input keys exists."""

        keys = set(self.redis_client.scan_iter())

        diff = [
            elem 
            for elem in keys 
            if elem not in elem_input
        ]

        return diff

