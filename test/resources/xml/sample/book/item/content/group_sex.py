from mugimugi.entity.main.book import Content
from mugimugi.enum import Ratio

from .......configuration import SAMPLE
from ....abstract import Sample


class BookContentGroupSex(Sample):
    file_path = SAMPLE / "book/item/content/group_sex.xml"
    type = Content
    object = Content(
        english_name="Group Sex",
        japanese_name="グループセックス",
        romaji_name="",
        other_names=["乱交"],
        _id="K66",
        version=4,
        objects_count=39263,
        ratio=Ratio.NOT_SET,
    )
