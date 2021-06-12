from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Iterator

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi.enum import ElementPrefix


@dataclass
class Element:
    mugimugi_id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"[{''.join(ElementPrefix.values())}]\d+",
        ),
    )
    id: int = None
    prefix: ElementPrefix = None

    english_name: str = field(
        default="", metadata=dict(name="NAME_EN", type=XmlType.ELEMENT, required=True)
    )
    japanese_name: str = field(
        default="", metadata=dict(name="NAME_JP", type=XmlType.ELEMENT, required=True)
    )
    romaji_name: str = field(
        default="", metadata=dict(name="NAME_R", type=XmlType.ELEMENT, required=True)
    )
    other_names: list[str] = field(
        default_factory=list,
        metadata=dict(name="NAME_ALT", type=XmlType.ELEMENT, min_occurs=0),
    )

    def __post_init__(self):
        id_ = self.mugimugi_id
        self.id = int(id_[1:])
        if self.prefix is None:
            self.prefix = ElementPrefix(id_[0])

    @property
    def names(self) -> Iterator[str]:
        if name := self.japanese_name:
            yield name
        if name := self.romaji_name:
            yield name
        if name := self.english_name:
            yield name
        for name in self.other_names:
            if name:
                yield name

    @classmethod
    @property
    @abstractmethod
    def PREFIX(cls) -> ElementPrefix:
        ...
