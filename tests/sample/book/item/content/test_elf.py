from unittest.case import TestCase

from mugimugi.entity.book import Linker
from mugimugi.entity.item import LinkedPartialContent
from mugimugi.enum import Ratio

from .....configuration import SAMPLE
from ....sample import Sample


class TestBookContentElf(Sample, TestCase):
    file_path = SAMPLE / "book/item/content/elf.xml"
    type = LinkedPartialContent
    object = LinkedPartialContent(
        english_name="Elf",
        japanese_name="エルフ",
        romaji_name="",
        other_names=[],
        _id="K39",
        version=1,
        objects_count=2803,
        ratio=Ratio.NOT_SET,
    )


class TestBookContentElfFromUnion(Sample):

    file_path = SAMPLE / "book/item/elf.xml"
    type = Linker
    object = Linker(
        [
            LinkedPartialContent(
                english_name="Elf",
                japanese_name="エルフ",
                romaji_name="",
                other_names=[],
                _id="K39",
                version=1,
                objects_count=2803,
                ratio=Ratio.NOT_SET,
            )
        ]
    )
