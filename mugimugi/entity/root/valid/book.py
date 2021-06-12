from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Book
from .abstract import ValidRoot


@dataclass
class BookRoot(ValidRoot[Book]):
    elements: list[Book] = field(
        default_factory=list,
        metadata=dict(name=Book.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
