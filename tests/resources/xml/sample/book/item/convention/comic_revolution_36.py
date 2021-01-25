from datetime import date

from mugimugi.entity.main.book import Convention

from .......configuration import SAMPLE
from ....sample import Sample


class BookConventionComicRevolution36(Sample):
    file_path = SAMPLE / "book/item/convention/comic_revolution_36.xml"
    type = Convention
    object = Convention(
        english_name="Comic Revolution 36",
        japanese_name="コミックレヴォリューション 36",
        romaji_name="コミックレヴォリューション36",
        other_names=[],
        _id="N107",
        version=2,
        objects_count=696,
        date_start=date(2004, 10, 3),
        date_end=date(2004, 10, 3),
    )
