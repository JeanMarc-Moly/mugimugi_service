from test.resources.xml.sample.book.item.imprint.no import BookImprintNo
from unittest.case import TestCase

from ....abstract import Sample


class TestBookImprintNo(BookImprintNo, Sample, TestCase):
    ...
