from unittest.case import TestCase

from tests.resources.xml.sample.book.item.parody.fate_stay_night import (
    BookParodyFateStayNight,
)

from ....sample import Sample


class TestBookParodyFateStayNight(BookParodyFateStayNight, Sample, TestCase):
    ...
