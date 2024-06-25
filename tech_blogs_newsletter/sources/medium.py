import json
import requests
from datetime import datetime
from http import HTTPStatus
from typing import Dict

from tech_blogs_newsletter.domain import Blog


def get_blog(blog_id: str) -> Blog:

    response = _request_posts(blog_id)

    blog_slug = response["payload"]["references"]["Collection"][blog_id]["slug"]

    blog = Blog()
    for post in response["payload"]["references"]["Post"].values():

        title = post["title"]
        publication_date = _convert_unix_timestamp_to_datetime(post["firstPublishedAt"])
        url = _create_post_url(blog_slug, post["uniqueSlug"])

        blog.add_post(title, publication_date, url)

    return blog


def _request_posts(blog_id: str) -> Dict:

    MEDIUM_COLLECTIONS_URL = "https://medium.com/_/api/collections/{}/stream"
    response = requests.get(url=MEDIUM_COLLECTIONS_URL.format(blog_id))

    if response.status_code == HTTPStatus.NOT_FOUND:
        raise BlogDoesNotExist(blog_id)

    return _convert_posts_response_to_dict(response)


def _convert_posts_response_to_dict(response: requests.Response) -> Dict:
    NON_JSON_RESPONSE_PREFIX = "])}while(1);</x>"
    data = response.text
    data = data.replace(NON_JSON_RESPONSE_PREFIX, "")
    return json.loads(data)


def _convert_unix_timestamp_to_datetime(unix_timestamp_in_milliseconds: str) -> datetime:
    unix_timestamp = unix_timestamp_in_milliseconds / 1000
    return datetime.utcfromtimestamp(unix_timestamp)


def _create_post_url(blog_slug: str, post_slug: str) -> str:
    MEDIUM_URL = "https://medium.com"
    return f"{MEDIUM_URL}/{blog_slug}/{post_slug}"


class BlogDoesNotExist(Exception):
    def __init__(self, blog_id: str):
        message = f"Blog ID {blog_id!r} does not exist."
        super().__init__(message)
