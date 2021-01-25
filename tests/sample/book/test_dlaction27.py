from unittest.case import TestCase

from tests.resources.xml.sample.book.item.publisher.no import BookPublisherNo

from ..sample import Sample


class TestBookPublisherNo(Sample, TestCase, BookPublisherNo):
    ...
