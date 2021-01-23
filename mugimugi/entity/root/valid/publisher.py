from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Publisher
from .abstract import ValidRoot


@dataclass
class PublisherRoot(ValidRoot[Publisher]):
    elements: list[Publisher] = field(
        default_factory=list,
        metadata=dict(name=Publisher.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
