from freezegun import freeze_time

from tech_blogs_newsletter import main
from tech_blogs_newsletter.domain import Blog, Post


@freeze_time("1900-01-01")
def test_search_new_tech_blogs_should_return_a_list_of_posts_for_every_tech_blog():

    newsletter = main.search_new_tech_blogs()

    for tech_blog_instance in main.TECH_BLOGS:
        blog = newsletter.get_blog(tech_blog_instance.name)
        assert isinstance(blog, Blog)
        assert len(blog) > 0
        for post in blog:
            assert isinstance(post, Post)


def test_search_new_tech_blogs_should_filter_posts_by_publication_date():

    newsletter = main.search_new_tech_blogs(max_days_since_publication=0)

    for tech_blog_instance in main.TECH_BLOGS:
        assert len(newsletter.get_blog(tech_blog_instance.name)) == 0
