from mugimugi.entity.main.book import Type

from .......configuration import SAMPLE
from ....abstract import Sample


class BookTypeDoujinshi(Sample):
    file_path = SAMPLE / "book/item/type/doujinshi.xml"
    type = Type
    object = Type(
        english_name="Doujinshi",
        japanese_name="同人誌",
        romaji_name="",
        other_names=[],
        _id="T1",
        version=1,
        objects_count=1329929,
    )
