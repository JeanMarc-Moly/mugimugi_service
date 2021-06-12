from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ..main import User
from .abstract import AbstractRoot


@dataclass
class EmptyRoot(AbstractRoot):
    user: User = field(
        metadata=dict(name=User.Meta.name, type=XmlType.ELEMENT, required=True)
    )
