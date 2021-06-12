from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import TypeCommon
from .abstract import LinkedPartialItem


@dataclass
class Type(TypeCommon, LinkedPartialItem):
    # FRQ present but useless
    _: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
