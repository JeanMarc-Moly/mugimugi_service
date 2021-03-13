from mugimugi.entity.main.book import Publisher

from .......configuration import SAMPLE
from ....abstract import Sample


class BookPublisherNo(Sample):
    file_path = SAMPLE / "book/item/publisher/no.xml"
    type = Publisher
    object = Publisher(
        english_name="No Publisher",
        japanese_name="出版社なし",
        romaji_name="",
        other_names=[],
        _id="L3",
        version=2,
        objects_count=1492741,
    )
