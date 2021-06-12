from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...main import Character
from .abstract import ValidRoot


@dataclass
class CharacterRoot(ValidRoot[Character]):
    elements: list[Character] = field(
        default_factory=list,
        metadata=dict(name=Character.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
