from typing import Dict, List, Union
from datetime import datetime

from dataclasses import dataclass

@dataclass
class CommandResult:
    """Dataclass for representing command result."""
    is_success: bool
    command: str
    message: str
    path: str
    attributes: Union[List[str], Dict[str, str]]
    execution_time: datetime = datetime.now()
