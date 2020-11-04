from typing import TypeVar
from xsdata.formats.converter import Converter, converter


Percent = TypeVar("Percent", bound=str)


class PercentConverter(Converter):
    @staticmethod
    def from_string(value: Percent, **_) -> float:
        return float(value.removesuffix("%"))

    @staticmethod
    def to_string(value: float, **_) -> Percent:
        return f"{value:.2f}%"


converter.register_converter(Percent, PercentConverter())
