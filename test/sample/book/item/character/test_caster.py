from test.resources.xml.sample.book.item.character.caster import BookCharacterCaster
from unittest.case import TestCase

from ....abstract import Sample


class TestBookCharacterCaster(BookCharacterCaster, Sample, TestCase):
    ...
