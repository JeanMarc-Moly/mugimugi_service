from mugimugi.entity.main.book import Circle
from mugimugi.enum.position import Position

from ......configuration import SAMPLE
from ...abstract import Sample


class BookCircleDigitalLover(Sample):
    file_path = SAMPLE / "book/item/circle/digital_lover.xml"
    type = Circle
    object = Circle(
        english_name="Digital Lover",
        japanese_name="Digital Lover",
        romaji_name="デジタルラバー",
        other_names=[],
        _id="C180",
        version=17,
        objects_count=421,
        parent=0,
        position=Position.MAIN,
    )
