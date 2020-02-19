# -*- coding: utf-8 -*-
import os
from typing import Dict, Set

from server import redis_client

class RedisService:
    """Service for working with Redis."""

    def save_dict(self, input: Dict[int, str]) -> None:
        """Save ids and file_paths to redis."""

        for key, value in input.items():
            redis_client.set(str(key), value)

    def validate_for_keys(self, elem_input: Set[str]) -> bool:
        """Validate, if all input keys exists."""

        keys = set(redis_client.scan_iter())

        diff = keys - elem_input

        return not bool(diff)

