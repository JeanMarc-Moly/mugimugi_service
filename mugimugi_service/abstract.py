from dataclasses import dataclass

from .api import API


@dataclass
class AbstractService:
    _api: API
