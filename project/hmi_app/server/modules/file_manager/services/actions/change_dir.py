
from pathlib import Path

from server import redis_client, base_path

from server.modules.file_manager.dto import CommandResult
from server.modules.file_manager.services.actions import BaseCommand

class ChangeDirectoryCommand(BaseCommand):
    """Command for changing current directory"""

    def __init__(self, command: str):
        self.command = command.replace('go', '')

        self.current_path = redis_client.get('current_path')

        if not self.current_path:
            self.current_path = base_path

    def process(self) -> CommandResult:

        path = Path(self.current_path) / Path(self.command)

        if path.exists():
            redis_client.set('current_path', str(path))

        return CommandResult(
            is_success=path.exists(),
            command = f'go {self.command}',
            path=self.current_path,
            message='Directory change result',
            attributes=[]
        )
