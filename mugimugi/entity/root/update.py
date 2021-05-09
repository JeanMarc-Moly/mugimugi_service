from dataclasses import dataclass, field
from enum import Enum

from ...entity.root.empty import EmptyRoot, XmlType


@dataclass
class UpdateRoot(EmptyRoot):
    @dataclass
    class Update:
        class Status(Enum):
            OK = "OK"

        status: Status = field(
            metadata=dict(name="STATUS", type=XmlType.ELEMENT, required=True),
        )

    update: Update = field(
        metadata=dict(name="UPDATE", type=XmlType.ELEMENT, required=True),
    )

    @property
    def is_ok(self) -> bool:
        return self.update.status is self.update.Status.OK
