from unittest.case import TestCase

from tests.resources.xml.sample.book.item.character.caster import BookCharacterCaster

from ....sample import Sample


class TestBookCharacterCaster(BookCharacterCaster, Sample, TestCase):
    ...
