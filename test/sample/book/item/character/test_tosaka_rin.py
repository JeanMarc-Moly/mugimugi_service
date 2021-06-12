from test.resources.xml.sample.book.item.character.tosaka_rin import (
    BookCharacterTosakaRin,
)
from unittest.case import TestCase

from ....abstract import Sample


class TestBookCharacterTosakaRin(BookCharacterTosakaRin, Sample, TestCase):
    ...
