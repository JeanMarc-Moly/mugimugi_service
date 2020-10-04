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
    :ivar date_start:
    :ivar date_end:
    :ivar id:
    :ivar ver:
    :ivar type:
    :ivar frq:
    :ivar parent:
    """
    class Meta:
        name = "ITEM"

    name_en: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME_EN",
            type="Element",
            namespace="",
            required=True
        )
    )
    name_jp: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME_JP",
            type="Element",
            namespace="",
            required=True
        )
    )
    name_r: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NAME_R",
            type="Element",
            namespace="",
            required=True
        )
    )
    objects: Optional[int] = field(
        default=None,
        metadata=dict(
            name="OBJECTS",
            type="Element",
            namespace="",
            required=True
        )
    )
    name_alt: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="NAME_ALT",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    date_start: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DATE_START",
            type="Element",
            namespace="",
            required=True
        )
    )
    date_end: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DATE_END",
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute",
            required=True,
            pattern=r"N\d+"
        )
    )
    ver: Optional[int] = field(
        default=None,
        metadata=dict(
            name="VER",
            type="Attribute",
            required=True
        )
    )
    type: str = field(
        init=False,
        default="convention",
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )
    frq: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type="Attribute",
            required=True
        )
    )
    parent: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PARENT",
            type="Attribute"
        )
    )
