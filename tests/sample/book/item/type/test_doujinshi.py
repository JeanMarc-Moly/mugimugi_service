from unittest.case import TestCase

from tests.resources.xml.sample.book.item.type.doujinshi import BookTypeDoujinshi

from ....sample import Sample


class TestBookTypeDoujinshi(BookTypeDoujinshi, Sample, TestCase):
    ...
