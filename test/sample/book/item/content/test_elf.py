from test.resources.xml.sample.book.item.content.elf import BookContentElf
from unittest.case import TestCase

from ....abstract import Sample


class TestBookContentElf(BookContentElf, Sample, TestCase):
    ...
