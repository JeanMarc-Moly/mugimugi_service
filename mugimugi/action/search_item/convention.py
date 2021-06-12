from dataclasses import dataclass, field
from datetime import date
from typing import Iterator, Optional, Union

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Convention
from ...entity.root import ValidRoot
from ...entity.utils.converter import Date
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchConvention(SearchItem):
    @dataclass
    class Root(ValidRoot[Convention]):
        elements: list[Convention] = field(
            default_factory=list,
            metadata=dict(
                name=Convention.Meta.name, type=XmlType.ELEMENT, min_occurs=0
            ),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CONVENTION, init=False)

    date_: Optional[date] = None

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Convention.PREFIX

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()

        if (date_ := self.date_) is not None:
            yield self.Parameter.DATE.value, f"{date_:Date.FORMAT}"
