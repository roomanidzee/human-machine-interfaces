# -*- coding: utf-8 -*-
import os
from typing import List

from flask import current_app

from server import base_path
from server.modules.numbers.dto import FileObject

class FilesService:
    """Service for working with files."""

    def __init__(self, img_path):
        """Constructor for working with images"""
        self.img_path = f'{base_path}/modules/numbers/{img_path}'

    def retrieve_all_files(self) -> List[FileObject]:
        """Retrieve all pictures of numbers."""
        files = [
            elem
            for elem in os.listdir(self.img_path)
            if 'gitkeep' not in elem
        ]

        return [
            FileObject(elem).path
            for elem in files
        ]
