from abc import ABC
from dataclasses import dataclass

from ..utils.xml import parse

from ...enum import ElementNode


@dataclass
class AbstractRoot(ABC):
    class Meta:
        name = ElementNode.LIST.value

    @classmethod
    def parse(cls, xml: str):
        return parse(cls, xml)
