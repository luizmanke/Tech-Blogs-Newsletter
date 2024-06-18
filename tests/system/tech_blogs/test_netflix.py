from typing import List

from tech_blogs_newsletter.tech_blogs.base import Post
from tech_blogs_newsletter.tech_blogs.netflix import Netflix


def test_get_netflix_posts_should_return_a_list_of_posts():

    posts = Netflix().get_posts()

    assert isinstance(posts, List)
    assert len(posts) > 0
    for post in posts:
        assert isinstance(post, Post)
