from typing import Dict
from datetime import datetime

from dataclasses import dataclass

@dataclass
class CommandResult:
    """Dataclass for representing command result."""
    is_success: bool
    command: str
    message: str
    attributes: Dict[str, str]
    execution_time: datetime
