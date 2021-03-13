from test.resources.xml.sample.book.item.type.doujinshi import BookTypeDoujinshi
from unittest.case import TestCase

from ....abstract import Sample


class TestBookTypeDoujinshi(BookTypeDoujinshi, Sample, TestCase):
    ...
