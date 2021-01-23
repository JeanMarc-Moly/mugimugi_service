from dataclasses import dataclass

from ...common import ContentCommon
from .abstract import SubItem


@dataclass
class SubContent(ContentCommon, SubItem):
    ...
