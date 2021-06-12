from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Content
from .abstract import ValidRoot


@dataclass
class ContentRoot(ValidRoot[Content]):
    elements: list[Content] = field(
        default_factory=list,
        metadata=dict(name=Content.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
