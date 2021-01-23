from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi.enum import ElementNode
from mugimugi.enum import Error as ErrorEnum
from mugimugi.error import *

CONVERTER = {
    ErrorEnum.UNKNOWN: Unknown,
    ErrorEnum.NO_QUERY_LEFT: NoQueryLeft,
    ErrorEnum.INVALID_SCORE: InvalidScore,
    ErrorEnum.API_KEY_NOT_FOUND: ApiKeyNotFound,
    ErrorEnum.ID_NOT_FOUND: IdNotFound,
    ErrorEnum.OBJECT_NOT_FOUND: ObjectNotFound,
    ErrorEnum.USER_NOT_FOUND: UserNotFound,
    ErrorEnum.IMAGE_NOT_FOUND: ImageNotFound,
    ErrorEnum.IMAGE_NOT_RECEIVED: ImageNotReceived,
    ErrorEnum.IMAGE_NOT_UPLOADED: ImageNotUploaded,
    ErrorEnum.IMAGE_SEARCH_SERVER_DOWN: ImageServerDown,
    ErrorEnum.IMAGE_TOO_BIG: ImageTooBig,
}


@dataclass
class ErrorCommon:
    class Meta:
        name = ElementNode.ERROR.value

    id: int = field(
        metadata=dict(name="code", type="Attribute", required=True, min_inclusive=0)
    )
    description: str = field(metadata=dict(name="EXACT", type=XmlType.ELEMENT))
    declaration: str = field(metadata=dict(name="TYPE", type=XmlType.ELEMENT))
    exception: ErrorEnum = field(metadata=dict(name="CODE", type=XmlType.ELEMENT))

    def blow(self):
        raise CONVERTER[self.exception](self.description)
