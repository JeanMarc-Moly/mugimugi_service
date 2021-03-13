from test.resources.xml.sample.book.item.collection.dlaction import (
    BookCollectionDLAction,
)
from unittest.case import TestCase

from ....abstract import Sample


class TestBookCollectionDLAction(BookCollectionDLAction, Sample, TestCase):
    ...
