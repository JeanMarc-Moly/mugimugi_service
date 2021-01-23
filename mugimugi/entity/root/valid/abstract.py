from dataclasses import dataclass
from typing import Generic, TypeVar

from mugimugi.entity.root import EmptyRoot

E = TypeVar("E")


@dataclass
class ValidRoot(EmptyRoot, Generic[E]):
    elements: list[E]
