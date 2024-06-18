from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Post:
    title: str
    publication_date: datetime
    url: str


class TechBlog(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_posts(self) -> List[Post]:
        pass
