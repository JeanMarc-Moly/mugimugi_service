from typing import TypeVar

from xsdata.formats.converter import Converter, converter

Percent = TypeVar("Percent", bound=str)


class PercentConverter(Converter):
    @staticmethod
    def deserialize(value: Percent, **_) -> float:
        return float(value.removesuffix("%"))

    @staticmethod
    def serialize(value: float, **_) -> Percent:
        return f"{value:.2f}%"


converter.register_converter(Percent, PercentConverter())
