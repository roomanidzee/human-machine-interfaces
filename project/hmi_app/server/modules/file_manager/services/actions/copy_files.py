
from server.modules.file_manager.services.actions import BaseCommand

class FilesCopyCommand(BaseCommand):
    """Command for copying files in directory"""

    def __init__(self, command: str):
        self.command = command
