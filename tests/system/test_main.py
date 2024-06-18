from typing import Dict, List

from tech_blogs_newsletter import main
from tech_blogs_newsletter.domain import Blog, Newsletter


def test_search_posts_should_return_a_list_of_posts_for_every_tech_blog():

    newsletter = main.search_tech_blogs()

    assert isinstance(newsletter, Newsletter)
    for tech_blog in main.TECH_BLOGS:
        assert tech_blog.name in newsletter
        assert isinstance(newsletter.get_blog(tech_blog.name), Blog)
