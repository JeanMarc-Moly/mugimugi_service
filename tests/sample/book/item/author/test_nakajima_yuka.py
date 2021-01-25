from unittest.case import TestCase

from tests.resources.xml.sample.book.item.author.nakajima_yuka import (
    BookAuthorNakajimaYuka,
)

from ....sample import Sample


class TestBookAuthorNakajimaYuka(BookAuthorNakajimaYuka, Sample, TestCase):
    ...
