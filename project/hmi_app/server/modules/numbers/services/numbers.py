# -*- coding: utf-8 -*-

import random
from typing import Dict, List, Set

class NumbersService:
    """Service for worling with numbers."""

    def generate_random_numbers() -> Set[int]:
        """Create a set with 5 random numbers."""

        return {
            random.randrange(1, 10)
            for _ in range(5)
        }

    def create_dict(
        numbers: Set[int],
        file_paths: List[str]
    ) -> Dict[int, str]:
        """Create a dict with number as a key and file_path as a value"""

        if max(numbers) != len(file_paths):
            raise ValueError('Incorrect input for numbers and file_paths')

        result = {}

        for elem in numbers:
            result[elem] = file_paths[elem]

        return result
