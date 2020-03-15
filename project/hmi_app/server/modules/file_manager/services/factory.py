
from server.modules.file_manager.dto import CommandResult

from server.modules.file_manager.services.actions import (
    FilesListCommand,
    ChangeDirectoryCommand,
    FileCreateCommand,
    FilesCopyCommand
)

def process_command(command: str) -> CommandResult:

    command_handler = None

    if command.startswith('list'):
        command_handler = FilesListCommand(command)
    elif command.startswith('go'):
        command_handler = ChangeDirectoryCommand(command)
    elif command.startswith('create'):
        command_handler = FileCreateCommand(command)
    elif command.startswith('copy'):
        command_handler = FilesCopyCommand(command)
    else:
        raise ValueError(f'Wrong command input: {command}')

    return command_handler.process()
