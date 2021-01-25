from unittest.case import TestCase

from tests.resources.xml.sample.book.item.character.tosaka_rin import (
    BookCharacterTosakaRin,
)

from ....sample import Sample


class TestBookCharacterTosakaRin(BookCharacterTosakaRin, Sample, TestCase):
    ...
