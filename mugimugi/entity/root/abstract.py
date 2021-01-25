from abc import ABC
from dataclasses import dataclass

from ...enum import ElementNode
from ..utils.xml import parse


@dataclass
class AbstractRoot(ABC):
    class Meta:
        name = ElementNode.LIST.value

    @classmethod
    def parse(cls, xml: str):
        return parse(cls, xml)
