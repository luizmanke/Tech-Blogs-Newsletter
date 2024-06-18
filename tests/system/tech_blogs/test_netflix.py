from typing import List

from tech_blogs_newsletter.domain import Blog, Post
from tech_blogs_newsletter.tech_blogs.netflix import Netflix


def test_netflix_get_blog_should_return_a_list_of_posts():

    blog = Netflix().get_blog()

    assert isinstance(blog, Blog)
    assert len(blog) > 0
    for post in blog:
        assert isinstance(post, Post)
