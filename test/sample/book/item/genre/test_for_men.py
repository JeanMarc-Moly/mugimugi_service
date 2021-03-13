from test.resources.xml.sample.book.item.genre.for_men import BookGenreForMen
from unittest.case import TestCase

from ....abstract import Sample


class TestBookGenreForMen(BookGenreForMen, Sample, TestCase):
    ...
