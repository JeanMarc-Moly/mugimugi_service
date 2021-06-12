from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Parody
from .abstract import ValidRoot


@dataclass
class ParodyRoot(ValidRoot[Parody]):
    elements: list[Parody] = field(
        default_factory=list,
        metadata=dict(name=Parody.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
