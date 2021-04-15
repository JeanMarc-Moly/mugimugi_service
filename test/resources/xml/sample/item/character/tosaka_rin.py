from mugimugi.entity.main.book import Character
from mugimugi.enum import Ratio
from mugimugi.enum.gender import Sex

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCharacterTosakaRin(Sample):
    file_path = SAMPLE / "book/item/character/tosaka_rin.xml"
    type = Character
    object = Character(
        english_name="Tōsaka Rin",
        japanese_name="遠坂凛",
        romaji_name="トオサカリン",
        other_names=["Tosaka Rin", "Tousaka Rin", "Tohsaka Rin"],
        _id="H211",
        version=19,
        objects_count=979,
        sex=Sex.FEMALE,
        age="",
        ratio=Ratio.NOT_SET,
    )
