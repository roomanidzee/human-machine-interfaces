
from pathlib import Path

from server import redis_client, base_path
from server.modules.file_manager.dto import CommandResult
from server.modules.file_manager.services.actions import BaseCommand

class FileCreateCommand(BaseCommand):
    """Command for file create in path"""

    def __init__(self, command: str):
        self.command = command.replace('create', '')

        self.current_path = redis_client.get('current_path')

        if not self.current_path:
            self.current_path = base_path

        self.command_args = self.command.split(' ')
    
    def process(self) -> CommandResult:

        folder_path = ""

        try:
            folder_path = self.command_args[self.command_args.index('-p') + 1]
        except ValueError:
            folder_path = self.current_path

        try:
            file_path = self.command_args[self.command_args.index('-f') + 1]

            new_path = Path(path) / Path(new_file)
            new_path.touch()

        except:

            return CommandResult(
                is_success=False,
                command=f'create {self.command}',
                path=folder_path,
                message='File create result',
                attributes=[str(new_path)]
            )

        return CommandResult(
            is_success=True,
            command=f'create {self.command}',
            path=folder_path,
            message='File create result',
            attributes=[str(new_path)]
        )
