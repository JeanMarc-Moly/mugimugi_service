from mugimugi.entity.main.book import Parody
from mugimugi.enum import Ratio

from .......configuration import SAMPLE
from ....abstract import Sample


class BookParodyFateStayNight(Sample):
    file_path = SAMPLE / "book/item/parody/fate_stay_night.xml"
    type = Parody
    object = Parody(
        english_name="Fate/stay night",
        japanese_name="Fate/stay night",
        romaji_name="フェイトステイナイト",
        other_names=[],
        _id="P16",
        version=29,
        objects_count=5268,
        ratio=Ratio.NOT_SET,
    )
