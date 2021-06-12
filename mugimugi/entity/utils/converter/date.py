from datetime import date, datetime
from typing import Optional, TypeVar

from xsdata.formats.converter import Converter, converter

Date = date


class DateConverter(Converter):
    NO_DATE = "0000-00-00"
    FORMAT = "%Y-%m-%d"

    @classmethod
    def deserialize(cls, value: str, **_) -> Date:
        if value == cls.NO_DATE:
            return None
        return datetime.strptime(value, cls.FORMAT).date()

    @classmethod
    def serialize(cls, value: Optional[Date], **_) -> str:
        if value is None:
            return cls.NO_DATE
        return value.strftime(cls.FORMAT)


converter.register_converter(Date, DateConverter())
