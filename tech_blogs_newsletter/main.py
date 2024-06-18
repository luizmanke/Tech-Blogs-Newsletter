from typing import Dict, List

from tech_blogs_newsletter.tech_blogs import TECH_BLOGS
from tech_blogs_newsletter.tech_blogs.base import Post


def search_posts() -> Dict[str, List[Post]]:

    posts = {}
    for TechBlog in TECH_BLOGS:
        tech_blog = TechBlog()
        posts[tech_blog.name] = tech_blog.get_posts()

    return posts


if __name__ == "__main__":
    search_posts()
