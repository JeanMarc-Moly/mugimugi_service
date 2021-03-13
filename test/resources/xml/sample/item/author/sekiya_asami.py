from mugimugi.entity.main import Author
from mugimugi.entity.main.sub import SubContent

from ......configuration import SAMPLE
from ...abstract import Sample


class BookAuthorSekiyaAsami(Sample):
    file_path = SAMPLE / "item/author/sekiya_asami.xml"
    type = Author
    object = Author(
        _id="A1484",
        english_name="Sekiya Asami",
        japanese_name="関谷あさみ",
        romaji_name="セキヤアサミ",
        version=14,
        objects_count=217,
        _links=Author.Linker(
            items=[
                SubContent(
                    _id="K12",
                    english_name="Incest",
                    japanese_name="近親姦",
                    other_names=["近親相姦"],
                    version=5,
                    objects_count=13054,
                ),
                SubContent(
                    _id="K15",
                    english_name="Loli",
                    japanese_name="ロリ",
                    other_names=["lolicon", "lolikon", "rorikon", "ロリコン"],
                    version=3,
                    objects_count=74960,
                ),
                SubContent(
                    _id="K601",
                    english_name="School Girl",
                    japanese_name="女子生徒",
                    version=3,
                    objects_count=20327,
                ),
            ]
        ),
    )
