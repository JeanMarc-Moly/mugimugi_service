from dataclasses import dataclass
from typing import Callable


@dataclass
class AbstractService:
    _api: Callable
