from unittest.case import TestCase

from tests.resources.xml.sample.book.item.collection.dlaction import (
    BookCollectionDLAction,
)

from ....sample import Sample


class TestBookCollectionDLAction(BookCollectionDLAction, Sample, TestCase):
    ...
