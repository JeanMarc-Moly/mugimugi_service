from dataclasses import dataclass, field

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedItem, LinkedPartialItem


@dataclass
class AbstractGenre:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.GENRE.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.GENRE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Genre(AbstractGenre, Item):
    ...


@dataclass
class GenreRoot(ValidRoot[Genre]):
    elements: list[Genre] = field(
        default_factory=list,
        metadata=dict(name=Genre.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialGenre(AbstractGenre, LinkedPartialItem):
    ...
