from unittest.case import TestCase

from tests.resources.xml.sample.book.item.circle.digital_lover import (
    BookCircleDigitalLover,
)

from ....sample import Sample


class TestBookCircleDigitalLover(BookCircleDigitalLover, Sample, TestCase):
    ...
