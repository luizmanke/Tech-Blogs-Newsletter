from tech_blogs_newsletter.domain import Blog
from tech_blogs_newsletter.sources import medium
from tech_blogs_newsletter.tech_blogs.base import TechBlog


class Netflix(TechBlog):

    def __init__(self):
        super().__init__(name="Netflix")

    def get_blog(self) -> Blog:
        return medium.get_blog(blog_id="2615bd06b42e")
