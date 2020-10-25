from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Item:
    """
    :ivar name_en:
    :ivar name_jp:
    :ivar name_r:
    :ivar objects:
    :ivar name_alt:
    :ivar parent:
    :ivar ver:
    :ivar frq:
    :ivar id:
    :ivar type:
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
    name_alt: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NAME_ALT",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
        ),
    )
    parent: Optional[int] = field(
        default=None,
        metadata=dict(name="PARENT", type="Attribute", required=True, min_inclusive=0),
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
    id: Optional[str] = field(
        default=None,
        metadata=dict(name="ID", type="Attribute", required=True, pattern=r"P\d+"),
    )
    type: str = field(
        init=False,
        default="parody",
        metadata=dict(name="TYPE", type="Attribute", required=True),
    )
