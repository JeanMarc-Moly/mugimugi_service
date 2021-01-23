from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ..main import Error
from .abstract import AbstractRoot


@dataclass
class FailedRoot(AbstractRoot):
    error: Error = field(
        metadata=dict(name=Error.Meta.name, type=XmlType.ELEMENT, required=True)
    )
