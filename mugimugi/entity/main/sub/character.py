from dataclasses import dataclass

from ...common import CharacterCommon
from .abstract import SubItem


@dataclass
class SubCharacter(CharacterCommon, SubItem):
    ...
