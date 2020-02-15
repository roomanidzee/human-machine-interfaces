# -*- coding: utf-8 -*-
import os
from typing import List

from flask import current_app

from server.modules.numbers.dto import FileObject

class FilesService:
    """Service for working with files."""

    def __init__(self, img_path):
        """Constructor for working with images"""
        self.img_path = img_path

    def retrieve_all_files() -> List[FileObject]:
        """Retrieve all pictures of numbers."""
        files = os.listdir(self.img_path)

        return [
            FileObject(elem)
            for elem in files
        ]
