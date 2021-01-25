from unittest.case import TestCase

from tests.resources.xml.sample.book.item.genre.for_men import BookGenreForMen

from ....sample import Sample


class TestBookGenreForMen(BookGenreForMen, Sample, TestCase):
    ...
