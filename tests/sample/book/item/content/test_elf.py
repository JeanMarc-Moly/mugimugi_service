from unittest.case import TestCase

from tests.resources.xml.sample.book.item.content.elf import BookContentElf

from ....sample import Sample


class TestBookContentElf(BookContentElf, Sample, TestCase):
    ...
