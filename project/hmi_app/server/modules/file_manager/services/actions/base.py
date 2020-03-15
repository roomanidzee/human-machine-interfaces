
from server.modules.file_manager.dto import CommandResult

class BaseCommand:
    """Base class for file manager commands."""

    def __init__(self, command: str):
        """Initialization of class with his command."""
        self.command = command

    def process(self) -> CommandResult:
        """Method for processing input command."""
        raise NotImplementedError('Method is not implemented yet')

    def __repr__(self):
        return f'CommandClass(name={type(self).__name__}, command={self.command})'

    def __str__(self):
        return repr(self)
