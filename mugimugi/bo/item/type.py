from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Item:
    """
    :ivar id:
    :ivar type:
    :ivar parent:
    """

    class Meta:
        name = "ITEM"

    id: Optional[str] = field(
        default=None,
        metadata=dict(name="ID", type="Attribute", required=True, pattern=r"T\d+"),
    )
    type: str = field(
        init=False,
        default="type",
        metadata=dict(name="TYPE", type="Attribute", required=True),
    )
    parent: Optional[int] = field(
        default=None,
        metadata=dict(name="PARENT", type="Attribute", required=True, min_inclusive=0),
    )
