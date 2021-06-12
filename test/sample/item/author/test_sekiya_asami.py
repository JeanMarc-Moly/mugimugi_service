from test.resources.xml.sample.item.author.sekiya_asami import BookAuthorSekiyaAsami
from unittest.case import TestCase

from ...abstract import Sample


class TestBookAuthorNakajimaYuka(BookAuthorSekiyaAsami, Sample, TestCase):
    ...
