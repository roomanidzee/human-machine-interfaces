
from server.modules.file_manager.services.actions import BaseCommand

class FileCreateCommand(BaseCommand):
    """Command for file create in path"""

    def __init__(self, command: str):
        self.command = command