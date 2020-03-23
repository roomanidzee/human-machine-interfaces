
import argparse
from pathlib import Path

from server import redis_client
from server.modules.file_manager.services.actions import BaseCommand

class FileCreateCommand(BaseCommand):
    """Command for file create in path"""

    def __init__(self, command: str):
        self.command = command.replace('create', '')

        self.current_path = redis_client.get('current_path')

        if not self.current_path:
            self.current_path = base_path
        
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '-p',
            dest='path',
            type=str,
            default=self.current_path,
            help='Directory for file create'
        )

        parser.add_argument(
            '-f',
            dest='new_file',
            type=str,
            help='File for creation'
        )

        self.command_args = parser.parse_args([self.command])
    
    def process(self) -> CommandResult:

        path = self.command_args.path
        new_file = self.command_args.new_file

        new_path = Path(path) / Path(new_file)
        new_path.touch()

        return CommandResult(
            is_success=True,
            command=f'create {self.command}',
            path=self.command_args.path,
            message='File create result',
            attributes=[str(new_path)]
        )
