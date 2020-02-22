# -*- coding: utf-8 -*-

import random
from typing import Dict, List, Set

class NumbersService:
    """Service for working with numbers."""

    def __init__(self):
        self.IMAGE_COUNT = 49

    def generate_random_numbers(self) -> Set[int]:
        """Create a set with random numbers. Limit is IMAGE_COUNT"""

        return {
            random.randrange(1, self.IMAGE_COUNT)
            for _ in range(10)
        }

    def create_dict(
        self,
        numbers: Set[int],
        file_paths: List[str]
    ) -> Dict[int, str]:
        """Create a dict with number as a key and file_path as a value"""

        result = {}

        for elem in numbers:
            result[elem] = file_paths[random.randrange(1, 10)]
        
        return result
