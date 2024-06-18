from abc import ABC, abstractmethod

from tech_blogs_newsletter.domain import Blog


class TechBlog(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_blog(self) -> Blog:
        pass
