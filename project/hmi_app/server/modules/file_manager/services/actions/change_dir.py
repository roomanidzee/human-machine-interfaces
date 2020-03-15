
from server.modules.file_manager.services.actions import BaseCommand

class ChangeDirectoryCommand(BaseCommand):
    """Command for changing current directory"""

    def __init__(self, command: str):
        self.command = command