from mugimugi.entity.main.book import Genre
from mugimugi.enum import Ratio

from ......configuration import SAMPLE
from ...abstract import Sample


class BookGenreForMen(Sample):
    file_path = SAMPLE / "book/item/genre/for_men.xml"
    type = Genre
    object = Genre(
        english_name="For men",
        japanese_name="男性向け",
        romaji_name="",
        other_names=[],
        _id="G227",
        version=1,
        objects_count=346049,
        ratio=Ratio.NOT_SET,
    )
