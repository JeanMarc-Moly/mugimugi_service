from test.resources.xml.sample.book.item.publisher.no import BookPublisherNo
from unittest.case import TestCase

from ..abstract import Sample


class TestBookPublisherNo(Sample, TestCase, BookPublisherNo):
    ...
