from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    """This class represents an article."""

    title: str
    abstract: str
    authors: list
    published: datetime

    @property
    def description(self):
        title = f"Title: {self.title}"
        authors = f"Authors: {', '.join(self.authors)}"
        abstract = f"Abstract: {self.abstract}"
        return f"{title}. {authors}. {abstract}"
