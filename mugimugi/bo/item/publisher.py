from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Item:
    """
    :ivar name_en:
    :ivar name_jp:
    :ivar name_r:
    :ivar objects:
    :ivar id:
    :ivar type:
    :ivar ver:
    :ivar frq:
    """

    class Meta:
        name = "ITEM"

    name_en: Optional[str] = field(
        default=None,
        metadata=dict(name="NAME_EN", type="Element", namespace="", required=True),
    )
    name_jp: Optional[str] = field(
        default=None,
        metadata=dict(name="NAME_JP", type="Element", namespace="", required=True),
    )
    name_r: Optional[str] = field(
        default=None,
        metadata=dict(name="NAME_R", type="Element", namespace="", required=True),
    )
    objects: Optional[int] = field(
        default=None,
        metadata=dict(name="OBJECTS", type="Element", namespace="", required=True),
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(name="ID", type="Attribute", required=True, pattern=r"L\d+"),
    )
    type: str = field(
        init=False,
        default="publisher",
        metadata=dict(name="TYPE", type="Attribute", required=True),
    )
    ver: Optional[int] = field(
        default=None,
        metadata=dict(name="VER", type="Attribute", required=True, min_inclusive=0),
    )
    frq: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type="Attribute",
            required=True,
            min_inclusive=0,
            max_inclusive=5,
        ),
    )
