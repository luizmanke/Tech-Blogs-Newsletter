from datetime import datetime
from http import HTTPStatus

import pytest

from tech_blogs_newsletter.domain import Blog, Post
from tech_blogs_newsletter.sources import medium


def test_get_blog_should_return_a_list_with_every_post(requests_mock):

    requests_mock.get(
        url="https://medium.com/_/api/collections/fake-collection/stream",
        text="""
])}while(1);</x>{
    "payload": {
        "references": {
            "Collection": {
                "fake-collection": {
                    "slug": "fake-collection-slug"
                }
            },
            "Post": {
                "fake-post-1": {
                    "title": "Fake Post 1",
                    "firstPublishedAt": 1717791000000,
                    "uniqueSlug": "fake-post-1-slug"
                },
                "fake-post-2": {
                    "title": "Fake Post 2",
                    "firstPublishedAt": 1717669230000,
                    "uniqueSlug": "fake-post-2-slug"
                }
            }
        }
    }
}
        """,
    )

    blog = medium.get_blog(blog_id="fake-collection")

    assert blog == Blog([
        Post(
            title="Fake Post 1",
            publication_date=datetime(2024, 6, 7, 20, 10, 0),
            url="https://medium.com/fake-collection-slug/fake-post-1-slug",
        ),
        Post(
            title="Fake Post 2",
            publication_date=datetime(2024, 6, 6, 10, 20, 30),
            url="https://medium.com/fake-collection-slug/fake-post-2-slug",
        ),
    ])


def test_get_blog_should_raise_if_blog_does_not_exist(requests_mock):

    requests_mock.get(
        url="https://medium.com/_/api/collections/fake-collection/stream",
        status_code=HTTPStatus.NOT_FOUND,
    )

    with pytest.raises(medium.BlogDoesNotExist):
        medium.get_blog(blog_id="fake-collection")
