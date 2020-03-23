
import argparse
from pathlib import Path

from server import base_path, redis_client
from server.modules.file_manager.dto import CommandResult
from server.modules.file_manager.services.actions import BaseCommand

class FilesCopyCommand(BaseCommand):
    """Command for copying files in directory"""

    def __init__(self, command: str):
        self.command = command.replace('copy', '')

        self.current_path = redis_client.get('current_path')

        if not self.current_path:
            self.current_path = base_path

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-ids',
            dest='file_ids',
            type=list,
            help='Identificators for files'
        )

        parser.add_argument(
            '-p',
            dest='path',
            type=str,
            default=self.current_path,
            help='Directory for file list'
        )

        self.command_args = parser.parse_args([self.command])
    
    def process(self) -> CommandResult:

        keys = set(self.redis_client.scan_iter())

        file_keys = [
            elem
            for elem in keys
            if self.current_path in elem
        ]

        filtered_paths = [
            elem 
            for elem in file_keys
            if self.redis_client.get(elem) is not None
            and int(self.redis_client.get(elem)) in self.command_args.file_ids
        ]

        for elem in filtered_paths:
            src = Path(elem)
            dest = Path(f'{self.command_args.path}') / Path(f'{src.name}.{src.stem}')
            dest.write_bytes(src.read_bytes())

        return CommandResult(
            is_success=True,
            command=f'copy {self.command}',
            path=self.command_args.path,
            message='File copy result',
            attributes=filtered_paths
        )
