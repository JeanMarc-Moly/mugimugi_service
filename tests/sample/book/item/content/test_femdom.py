from unittest.case import TestCase

from tests.resources.xml.sample.book.item.content.femdom import BookContentFemdom

from ....sample import Sample


class TestBookContentFemdom(BookContentFemdom, Sample, TestCase):
    ...
