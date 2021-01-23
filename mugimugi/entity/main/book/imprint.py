from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...common import ImprintCommon
from .abstract import LinkedPartialItem


@dataclass
class Imprint(ImprintCommon, LinkedPartialItem):
    # FRQ present but useless
    _: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
