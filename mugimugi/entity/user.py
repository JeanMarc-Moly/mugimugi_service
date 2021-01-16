from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ..enum.element_node import ElementNode


@dataclass
class User:
    class Meta:
        name = ElementNode.USER.value

    id: int = field(
        metadata=dict(name="id", type="Attribute", required=True, min_inclusive=0)
    )
    name: str = field(metadata=dict(name="User", type=XmlType.ELEMENT, required=True))
    remaining_api_queries: int = field(
        metadata=dict(
            name="Queries", type=XmlType.ELEMENT, required=True, min_inclusive=0
        )
    )
    remaining_image_queries: int = field(
        metadata=dict(
            name="Image_Queries", type=XmlType.ELEMENT, required=True, min_inclusive=0
        )
    )
