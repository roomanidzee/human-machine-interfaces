from server.modules.file_manager.services.actions import BaseCommand

class FilesListCommand(BaseCommand):
    """Command for listing files in path"""

    def __init__(self, command: str):
        self.command = command