from datetime import datetime
from http import HTTPStatus

import pytest

from tech_blogs_newsletter.domain import Blog, Post
from tech_blogs_newsletter.sources import medium


def test_get_blog_should_return_a_list_with_every_post(requests_mock):

    requests_mock.get(
        url="https://medium.com/feed/@some-blog",
        text="""
<channel>
    <item>
        <title><![CDATA[Title 1]]></title>
        <link>https://link1.com</link>
        <pubDate>Fri, 07 Jun 2024 20:10:00 GMT</pubDate>
    </item>
    <item>
        <title><![CDATA[Title 2]]></title>
        <link>https://link2.com</link>
        <pubDate>Thu, 06 Jun 2024 10:20:30 GMT</pubDate>
    </item>
</channel>
        """,
    )

    blog = medium.get_blog(blog_name="some-blog")

    assert blog == Blog([
        Post(
            title="Title 1",
            publication_date=datetime(2024, 6, 7, 20, 10, 0),
            url="https://link1.com",
        ),
        Post(
            title="Title 2",
            publication_date=datetime(2024, 6, 6, 10, 20, 30),
            url="https://link2.com",
        ),
    ])


def test_get_blog_should_raise_if_blog_does_not_exist(requests_mock):

    requests_mock.get(
        url="https://medium.com/feed/@some-blog",
        status_code=HTTPStatus.NOT_FOUND,
    )

    with pytest.raises(medium.BlogDoesNotExist):
        medium.get_blog(blog_name="some-blog")
