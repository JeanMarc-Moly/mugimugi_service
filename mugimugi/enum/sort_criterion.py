from fast_enum import FastEnum


class SortCriterion(metaclass=FastEnum):
    TITLE = "title"
    JAPANESE_TITLE = "jtitle"
    PUBLISHED_DATE = "date"
    PAGES_COUNT = "pages"
    PAGE_VIEWS_COUNT = "page_views"
    SCORE = "score"
    SUBMITTED_DATE = "added"
    LAST_MODIFICATION_DATE = "changed"
    KATAKANA_TITLE = "kana"
