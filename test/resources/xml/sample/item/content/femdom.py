from mugimugi.entity.main.book import Content
from mugimugi.enum import Ratio

from ......configuration import SAMPLE
from ...abstract import Sample


class BookContentFemdom(Sample):
    file_path = SAMPLE / "book/item/content/femdom.xml"
    type = Content
    object = Content(
        english_name="Domination (Femdom)",
        japanese_name="女性支配・女王様・ドミナ",
        romaji_name="",
        other_names=[],
        _id="K48",
        version=2,
        objects_count=7083,
        ratio=Ratio.NOT_SET,
    )
