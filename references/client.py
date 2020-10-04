from io import StringIO
from typing import Iterable
from httpx import get
from urllib.parse import urljoin
from pendulum import Date
from xml.etree.ElementTree import ElementTree, parse

from .error import Error

from ..enum import (
    Action,
    ItemType,
    Match,
    ObjectType,
    ObjectSearchParameter,
    Score,
    SortCriterion,
    SortOrder,
    YesNo,
)


HOST_NAME = "https://www.doujinshi.org/"
API_KEY = "604a83a77edafe119e1d"
API_PATH = "api/"
ACTION_PARAMETER = "S"

API = urljoin(urljoin(HOST_NAME, API_PATH), API_KEY) + "/"


def add_user_list():
    raise NotImplementedError(Action.ADD_USER_LIST)
    return _get(Action.ADD_USER_LIST, params)


def delete_user_list():
    raise NotImplementedError(Action.DELETE_USER_LIST)
    return _get(Action.DELETE_USER_LIST, params)


def get_from_id():
    raise NotImplementedError(Action.GET_ID)
    return _get(Action.GET_ID, params)


def search_image():
    raise NotImplementedError(Action.SEARCH_IMAGE)
    return _get(Action.SEARCH_IMAGE, params)


def search_item(nature: ItemType):
    raise NotImplementedError(Action.SEARCH_ITEM)
    return _get(Action.SEARCH_ITEM, params)


def search_object(
    title: str = None,
    *,
    page: int = None,
    match: Match = Match.EXACT,
    is_adult_only: bool = None,
    is_anthology: bool = None,
    is_copy_book: bool = None,
    is_free: bool = None,
    object_type: ObjectType = None,
    date_from: Date = None,
    date_to: Date = None,
    circles: Iterable[str] = None,
    authors: Iterable[str] = None,
    parodies: Iterable[str] = None,
    characters: Iterable[str] = None,
    contents: Iterable[str] = None,
    genres: Iterable[str] = None,
    convention: str = None,
    collection: str = None,
    publisher: str = None,
    imprint: str = None,
    contributor: str = None,
    submitter: str = None,
    sort_criterion: SortCriterion = None,
    want_ascending_sort: bool = None,
    is_censored: bool = None
):
    p = ObjectSearchParameter
    y = YesNo.YES.value
    n = YesNo.NO.value
    params = {}
    if title:
        params[p.TITLE.value] = title
    if page:
        params["page"] = page
    if match:
        params[p.MATCH_TYPE.value] = match.value
    if is_adult_only is not None:
        params[p.IS_ADULT_ONLY.value] = y if is_adult_only else n
    if is_anthology is not None:
        params[p.IS_ANTHOLOGY.value] = y if is_anthology else n
    if is_copy_book is not None:
        params[p.IS_COPY_BOOK.value] = y if is_copy_book else n
    if is_free is not None:
        params[p.IS_FREE.value] = y if is_free else n
    if object_type:
        params[p.TYPE.value] = object_type.value
    if date_from:
        params[p.RELEASE_DATE_FROM.value] = date_from.to_date_string()
    if date_to:
        params[p.RELEASE_DATE_TO.value] = date_to.to_date_string()
    if circles:
        params[p.CIRCLES.value] = ",".join(circles)
    if authors:
        params[p.AUTHORS.value] = ",".join(authors)
    if parodies:
        params[p.PARODIES.value] = ",".join(parodies)
    if characters:
        params[p.CHARACTERS.value] = ",".join(characters)
    if contents:
        params[p.CONTENTS.value] = ",".join(contents)
    if genres:
        params[p.GENRES.value] = ",".join(genres)
    if convention:
        params[p.CONVENTION.value] = convention
    if collection:
        params[p.COLLECTION.value] = collection
    if publisher:
        params[p.PUBLISHER.value] = publisher
    if imprint:
        params[p.IMPRINT.value] = imprint
    if contributor:
        params[p.CONTRIBUTOR.value] = contributor
    if submitter:
        params[p.SUBMITTER.value] = submitter
    if sort_criterion:
        params[p.SORT_CRITERION.value] = sort_criterion
    if want_ascending_sort is not None:
        params[p.SORT_ORDER.value] = (
            SortOrder.ASCENDING.value
            if want_ascending_sort
            else SortOrder.DESCENDING.value
        )
    if is_censored is not None:
        params[p.IS_CENSORED.value] = y if is_censored else n
    return _get(Action.SEARCH_OBJECT, params)


def vote(score: Score):
    return _get(Action.VOTE, {"score": score.value})


def _get(action: Action, params: dict) -> ElementTree:
    params[ACTION_PARAMETER] = action.value
    res = get(API, params=params, timeout=None).text
    print(res)
    xml = parse(StringIO(res))
    _raise_exception_if_any(xml)
    return xml


def _raise_exception_if_any(xml: ElementTree) -> None:
    error = xml.getroot()[0]
    if error.tag == "ERROR":
        raise Error(error.attrib["code"]).error()
