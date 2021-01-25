from unittest.case import TestCase

from tests.resources.xml.sample.book.item.convention.comic_revolution_36 import (
    BookConventionComicRevolution36,
)

from ....sample import Sample


class TestBookConventionComicRevolution36(
    BookConventionComicRevolution36, Sample, TestCase
):
    ...
