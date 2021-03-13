from test.resources.xml.sample.book.item.circle.digital_lover import (
    BookCircleDigitalLover,
)
from unittest.case import TestCase

from ....abstract import Sample


class TestBookCircleDigitalLover(BookCircleDigitalLover, Sample, TestCase):
    ...
