
import argparse
from pathlib import Path

from server import base_path, redis_client
from server.modules.file_manager.dto import CommandResult
from server.modules.numbers.services import RedisService
from server.modules.file_manager.services.actions import BaseCommand

class FilesListCommand(BaseCommand):
    """Command for listing files in path"""

    def __init__(self, command: str):
        self.command = command.replace('list', '')
        self.redis_service = RedisService()

        current_path = redis_client.get('current_path')

        if not current_path:
            current_path = base_path

        parser = argparse.ArgumentParser()
        
        parser.add_argument(
            '-f',
            dest='format',
            type=str,
            help='Choose, by which extension you will filter files'
        )

        parser.add_argument(
            '-i',
            dest='show_info',
            type=bool,
            help='Show full info or not'
        )

        parser.add_argument(
            '-p',
            dest='path',
            type=str,
            default=current_path,
            help='Directory for file list'
        )

        parser.add_argument(
            '-sort',
            dest='sort_type',
            type=str,
            help='Sorting for files'
        )

        self.command_args = parser.parse_args([self.command])

    def process(self) -> CommandResult:

        files = Path(self.command_args.path).glob('**/*')

        cache_dict = {
            elem.absolute : num
            for num, elem in enumerate(working_path)
        }

        self.redis_service.save_dict(cache_dict)

        if self.command_args.format:
            files = [
                elem
                for elem in files
                if elem.suffix == self.command_args.format
            ]

        if self.command_args.sort_type == 'name':
            files = sorted(
                files,
                key=lambda item: item.name
            )
        elif self.command_args.sort_type == 'date':
            files = sorted(
                files,
                key=labmda item: item.stat().st_ctime
            )

        attributes = None

        if self.command_args.show_info:

            attributes = {
                elem.absolute: {
                    'name': elem.name,
                    'size': elem.size,
                    'created_time': elem.stat().st_ctime
                }

                for elem in files
            }
        else:
            attributes = [
                elem.absolute
                for elem in files
            ]

        return CommandResult(
            is_success=True,
            command=f'list {self.command}',
            path=self.command_args.path,
            message='Files list result',
            attributes=attributes
        )

