
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

        files = Path(str(folder_path).replace('b', '')).glob('**/*')

        cache_dict = {
            elem.absolute : num
            for num, elem in enumerate(files)
        }

        self.redis_service.save_dict(cache_dict)

        try:
            file_format = self.command_args[self.command_args.index('-f') + 1]

            files = [
                elem
                for elem in files
                if elem.suffix == file_format
            ]
        except ValueError:
            pass

        try:
            sort_type = self.command_args[self.command_args.index('-sort') + 1]

            if sort_type == 'name':
                files = sorted(
                    files,
                    key=lambda item: item.name
                )
            elif sort_type == 'date':
                files = sorted(
                    files,
                    key=lambda item: item.stat().st_ctime
                )
        except ValueError:
            pass

        attributes = None

        try:
            show_info = self.command_args[self.command_args.index('-sort')]

            attributes = {
                elem.absolute: {
                    'name': elem.name,
                    'size': elem.size,
                    'created_time': elem.stat().st_ctime
                }

                for elem in files
            }
        except ValueError:
            attributes = [
                elem.absolute
                for elem in files
            ]

        return CommandResult(
            is_success=True,
            command=f'list {self.command}',
            path=folder_path,
            message='Files list result',
            attributes=attributes
        )

