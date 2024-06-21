from tech_blogs_newsletter.domain import Newsletter
from tech_blogs_newsletter.tech_blogs.netflix import Netflix


TECH_BLOGS = [
    Netflix(),
]


def search_new_tech_blogs(max_days_since_publication: int = 7) -> Newsletter:

    newsletter = Newsletter()
    for tech_blog in TECH_BLOGS:
        newsletter.add_blog(
            blog_name=tech_blog.name,
            blog=tech_blog.get_blog()
        )

    newsletter.filter_by_publication_date(max_days_since_publication)

    print(newsletter)

    return newsletter


if __name__ == "__main__":
    search_new_tech_blogs()
