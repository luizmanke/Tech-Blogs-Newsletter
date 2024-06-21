from typing import Dict, List

from tech_blogs_newsletter import main
from tech_blogs_newsletter.domain import Blog, Post


def test_search_posts_should_return_a_list_of_posts_for_every_tech_blog():

    newsletter = main.search_tech_blogs()

    for tech_blog_instance in main.TECH_BLOGS:
        blog = newsletter.get_blog(tech_blog_instance.name)
        assert isinstance(blog, Blog)
        assert len(blog) > 0
        for post in blog:
            assert isinstance(post, Post)
