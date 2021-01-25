from datetime import date

from mugimugi.entity.main.book import *
from mugimugi.enum import Language

from .....configuration import SAMPLE
from ..sample import Sample
from .item.author.nakajima_yuka import BookAuthorNakajimaYuka
from .item.character.caster import BookCharacterCaster
from .item.character.tosaka_rin import BookCharacterTosakaRin
from .item.circle.digital_lover import BookCircleDigitalLover
from .item.collection.dlaction import BookCollectionDLAction
from .item.content.elf import BookContentElf
from .item.content.femdom import BookContentFemdom
from .item.content.group_sex import BookContentGroupSex
from .item.convention.comic_revolution_36 import BookConventionComicRevolution36
from .item.genre.for_men import BookGenreForMen
from .item.imprint.no import BookImprintNo
from .item.parody.fate_stay_night import BookParodyFateStayNight
from .item.publisher.no import BookPublisherNo
from .item.type.doujinshi import BookTypeDoujinshi


class BookDLAction27(Sample):
    file_path = SAMPLE / "book/dlaction27.xml"
    type = Book
    object = Book(
        english_name="D.L. action 27",
        japanese_name="D.L. action 27",
        romaji_name="ディーエルアクション27",
        other_names=[],
        _id="B65715",
        version=6,
        match_ratio=None,
        release_date=date(2004, 10, 3),
        isbn="",
        pages_count=28,
        is_adult=True,
        is_anthology=False,
        is_copybook=False,
        magazine=0,
        language=Language.JAPANESE,
        info="",
        _links=Book.Linker(
            items=[
                BookAuthorNakajimaYuka.object,
                BookCharacterCaster.object,
                BookCharacterTosakaRin.object,
                BookCircleDigitalLover.object,
                BookCollectionDLAction.object,
                BookContentElf.object,
                BookContentFemdom.object,
                BookContentGroupSex.object,
                BookConventionComicRevolution36.object,
                BookGenreForMen.object,
                BookImprintNo.object,
                BookParodyFateStayNight.object,
                BookPublisherNo.object,
                BookTypeDoujinshi.object,
            ]
        ),
    )
