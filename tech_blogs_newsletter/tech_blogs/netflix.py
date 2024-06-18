from typing import List

from tech_blogs_newsletter.sources import medium
from tech_blogs_newsletter.tech_blogs.base import Post, TechBlog


class Netflix(TechBlog):

    def __init__(self):
        super().__init__(name="Netflix")

    def get_posts(self) -> List[Post]:

        posts = []
        for post in medium.get_users_posts(user="netflixtechblog"):
            posts.append(
                Post(
                    title=post["title"],
                    publication_date=post["publication_date"],
                    url=post["url"],
                ),
            )

        return posts
