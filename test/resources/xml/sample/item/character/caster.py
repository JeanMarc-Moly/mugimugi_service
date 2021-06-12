from mugimugi.entity.main.book import Character
from mugimugi.enum import Ratio
from mugimugi.enum.gender import Sex

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCharacterCaster(Sample):
    file_path = SAMPLE / "book/item/character/caster.xml"
    type = Character
    object = Character(
        english_name="Caster",
        japanese_name="キャスター",
        romaji_name="キャスター",
        other_names=[],
        _id="H3465",
        version=13,
        objects_count=125,
        sex=Sex.FEMALE,
        age="",
        ratio=Ratio.NOT_SET,
    )
