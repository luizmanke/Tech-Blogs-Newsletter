import requests
from datetime import datetime
from http import HTTPStatus
from typing import Dict, List

from bs4 import BeautifulSoup


def get_users_posts(user: str) -> List[Dict]:

    MEDIUM_FEED_URL = "https://medium.com/feed"
    response = requests.get(url=f"{MEDIUM_FEED_URL}/@{user}")

    if response.status_code == HTTPStatus.NOT_FOUND:
        raise UserDoesNotExist(user)

    posts = []
    soup = BeautifulSoup(response.text, "xml")
    for item in soup.channel.find_all("item"):
        posts.append({
            "title": item.title.string,
            "publication_date": _convert_publication_date_to_datetime(item.pubDate.string),
            "url": item.link.string,
        })

    return posts


def _convert_publication_date_to_datetime(publication_date: str) -> datetime:
    STRING_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
    return datetime.strptime(publication_date, STRING_FORMAT)


class UserDoesNotExist(Exception):
    def __init__(self, user: str):
        message = f"User {user!r} does not exist."
        super().__init__(message)
