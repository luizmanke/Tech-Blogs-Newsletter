from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List


@dataclass
class Post:
    """A single post."""
    title: str
    publication_date: datetime
    url: str


class Blog(List):
    """A list of posts from the same blog."""

    def add_post(self, title: str, publication_date: datetime, url: str):
        self.append(
            Post(
                title,
                publication_date,
                url,
            ),
        )

    def filter_by_publication_date(self, max_days_since_publication: int):
        min_publication_date = datetime.utcnow() - timedelta(days=max_days_since_publication)
        filtered_posts = list(filter(lambda post: post.publication_date > min_publication_date, self))
        self.clear()
        self.extend(filtered_posts)


class Newsletter(Dict):
    """A collection of blogs."""

    def add_blog(self, blog_name: str, blog: Blog):
        self[blog_name] = blog

    def get_blog(self, blog_name: str) -> Blog:
        return self[blog_name]

    def filter_by_publication_date(self, max_days_since_publication: int):
        for blog in self.values():
            blog.filter_by_publication_date(max_days_since_publication)

    def to_html(self) -> str:

        html = "<h1><b>Tech Blogs Newsletter</b></h1>"

        for blog_name, blog in self.items():
            html += f"\n\n<h2>{blog_name}</h2>\n\n"

            if not blog:
                html += f"No posts found.<br><br>\n"
                continue

            for post in blog:
                publication_date = post.publication_date.strftime("%Y-%m-%d %H:%M:%S")
                html += f'<a href="{post.url}">({publication_date}) {post.title}</a><br><br>\n'

        return html
