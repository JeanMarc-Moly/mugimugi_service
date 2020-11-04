from typing import Optional
from datetime import date
from xsdata.formats.converter import Converter, converter


class DateConverter(Converter):
    @staticmethod
    def from_string(value: str, **_) -> Optional[date]:
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None

    @staticmethod
    def to_string(value: date, **_) -> str:
        return value.isoformat() if value else None


converter.register_converter(date, DateConverter())
