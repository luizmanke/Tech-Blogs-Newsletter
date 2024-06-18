from dataclasses import dataclass
from datetime import datetime
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


class Newsletter(Dict):
    """A collection of blogs."""

    def add_blog(self, blog_name: str, blog: Blog):
        self[blog_name] = blog

    def get_blog(self, blog_name: str) -> Blog:
        return self[blog_name]
