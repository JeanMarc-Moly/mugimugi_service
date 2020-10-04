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
    :ivar data_sex:
    :ivar ver:
    :ivar frq:
    :ivar date_age:
    :ivar id:
    :ivar type:
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
    data_sex: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DATA_SEX",
            type="Element",
            namespace="",
            required=True,
            min_inclusive=0,
            max_inclusive=4
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
    frq: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type="Attribute",
            required=True
        )
    )
    date_age: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DATE_AGE",
            type="Element",
            namespace="",
            required=True,
            pattern=r"\d{,10}"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute",
            required=True,
            pattern=r"H\d+"
        )
    )
    type: str = field(
        init=False,
        default="character",
        metadata=dict(
            name="TYPE",
            type="Attribute",
            required=True
        )
    )
