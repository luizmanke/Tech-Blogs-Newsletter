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
