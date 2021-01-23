from dataclasses import dataclass

from ...common import AuthorCommon
from .abstract import SubItem


@dataclass
class SubAuthor(AuthorCommon, SubItem):
    ...
