from unittest.case import TestCase

from tests.resources.xml.sample.book.item.imprint.no import BookImprintNo

from ....sample import Sample


class TestBookImprintNo(BookImprintNo, Sample, TestCase):
    ...
