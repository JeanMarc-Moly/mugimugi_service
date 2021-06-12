from test.resources.xml.sample.book.item.parody.fate_stay_night import (
    BookParodyFateStayNight,
)
from unittest.case import TestCase

from ....abstract import Sample


class TestBookParodyFateStayNight(BookParodyFateStayNight, Sample, TestCase):
    ...
