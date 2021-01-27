from unittest.case import TestCase

from tests.resources.xml.sample.item.author.sekiya_asami import BookAuthorSekiyaAsami

from ...sample import Sample


class TestBookAuthorNakajimaYuka(BookAuthorSekiyaAsami, Sample, TestCase):
    ...
