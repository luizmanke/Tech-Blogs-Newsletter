from tech_blogs_newsletter.domain import Newsletter
from tech_blogs_newsletter.tech_blogs.netflix import Netflix


TECH_BLOGS = [
    Netflix(),
]


def search_tech_blogs() -> Newsletter:

    newsletter = Newsletter()
    for tech_blog in TECH_BLOGS:
        newsletter.add_blog(
            blog_name=tech_blog.name,
            blog=tech_blog.get_blog()
        )

    print(newsletter)

    return newsletter


if __name__ == "__main__":
    search_tech_blogs()
