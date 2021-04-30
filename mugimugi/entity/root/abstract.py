from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import TypeVar

from ...enum import ElementNode
from ..utils.xml import parse


@dataclass
class AbstractRoot(ABC):
    class Meta:
        name = ElementNode.LIST.value

    @classmethod
    def parse(cls: U, xml: str) -> U:
        return parse(cls, xml)


U = TypeVar("U", bound=AbstractRoot)
