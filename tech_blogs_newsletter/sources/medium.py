import requests
from datetime import datetime
from http import HTTPStatus

from bs4 import BeautifulSoup

from tech_blogs_newsletter.domain import Blog


def get_blog(blog_name: str) -> Blog:

    MEDIUM_FEED_URL = "https://medium.com/feed"
    response = requests.get(url=f"{MEDIUM_FEED_URL}/@{blog_name}")

    if response.status_code == HTTPStatus.NOT_FOUND:
        raise BlogDoesNotExist(blog_name)

    blog = Blog()
    soup = BeautifulSoup(response.text, "xml")
    for item in soup.channel.find_all("item"):
        blog.add_post(
            title=item.title.string,
            publication_date=_convert_publication_date_to_datetime(item.pubDate.string),
            url=item.link.string,
        )

    return blog


def _convert_publication_date_to_datetime(publication_date: str) -> datetime:
    STRING_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
    return datetime.strptime(publication_date, STRING_FORMAT)


class BlogDoesNotExist(Exception):
    def __init__(self, blog_name: str):
        message = f"Blog {blog_name!r} does not exist."
        super().__init__(message)
