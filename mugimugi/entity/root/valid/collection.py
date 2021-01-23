from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Collection
from .abstract import ValidRoot


@dataclass
class CollectionRoot(ValidRoot[Collection]):
    elements: list[Collection] = field(
        default_factory=list,
        metadata=dict(name=Collection.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
