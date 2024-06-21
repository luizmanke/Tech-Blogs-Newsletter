from datetime import datetime

from freezegun import freeze_time

from tech_blogs_newsletter import domain


def test_blog_should_add_posts():

    blog = domain.Blog()
    blog.add_post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com")
    blog.add_post(title="Title 2", publication_date=datetime(2024, 6, 20), url="https://url2.com")

    assert blog == [
        domain.Post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com"),
        domain.Post(title="Title 2", publication_date=datetime(2024, 6, 20), url="https://url2.com"),
    ]


@freeze_time("2024-06-21")
def test_blog_should_filter_posts_by_publication_date():

    blog = domain.Blog()
    blog.add_post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com")
    blog.add_post(title="Title 2", publication_date=datetime(2024, 6, 7), url="https://url2.com")

    blog.filter_by_publication_date(max_days_since_publication=7)

    assert blog == [
        domain.Post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com"),
    ]


def test_newsletter_should_add_and_get_blogs():

    blog = domain.Blog()
    blog.add_post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com")

    newsletter = domain.Newsletter()
    newsletter.add_blog(blog_name="fake-name", blog=blog)

    assert newsletter.get_blog("fake-name") == blog


@freeze_time("2024-06-21")
def test_newsletter_should_filter_posts_by_publication_date():

    blog = domain.Blog()
    blog.add_post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com")
    blog.add_post(title="Title 2", publication_date=datetime(2024, 6, 7), url="https://url2.com")

    newsletter = domain.Newsletter()
    newsletter.add_blog(blog_name="fake-name", blog=blog)

    newsletter.filter_by_publication_date(max_days_since_publication=7)

    assert newsletter.get_blog("fake-name") == [
        domain.Post(title="Title 1", publication_date=datetime(2024, 6, 21), url="https://url1.com"),
    ]
