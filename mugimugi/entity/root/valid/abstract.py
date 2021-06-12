from dataclasses import dataclass
from typing import Generic, TypeVar

from ...common.abstract import Element
from ..empty import EmptyRoot

E = TypeVar("E", bound=Element)


@dataclass
class ValidRoot(EmptyRoot, Generic[E]):
    elements: list[E]
