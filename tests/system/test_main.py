from typing import Dict, List

from tech_blogs_newsletter import main
from tech_blogs_newsletter.tech_blogs import TECH_BLOGS


def test_search_posts_should_return_a_list_of_posts_for_every_tech_blog():

    posts = main.search_posts()

    assert isinstance(posts, Dict)
    for tech_blog in TECH_BLOGS:
        assert tech_blog in posts
        assert isinstance(posts[tech_blog], List)
