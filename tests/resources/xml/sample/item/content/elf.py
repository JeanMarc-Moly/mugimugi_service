from mugimugi.entity.main.book import Content
from mugimugi.enum import Ratio

from .......configuration import SAMPLE
from ....sample import Sample


class BookContentElf(Sample):
    file_path = SAMPLE / "book/item/content/elf.xml"
    type = Content
    object = Content(
        english_name="Elf",
        japanese_name="エルフ",
        romaji_name="",
        other_names=[],
        _id="K39",
        version=1,
        objects_count=2803,
        ratio=Ratio.NOT_SET,
    )
