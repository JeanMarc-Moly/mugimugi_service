from dataclasses import dataclass

from ...common import ParodyCommon
from .abstract import SubItem


@dataclass
class SubParody(ParodyCommon, SubItem):
    ...
