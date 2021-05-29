from collections.abc import Sequence
from datetime import datetime, timezone


class SearchResults(Sequence):
    """SearchResults represents a sequence of articles come out from a
    search query."""

    def __init__(self, query, *articles):
        self.query = query
        self._articles = list(articles)

    def __len__(self):
        return len(self._articles)

    def __getitem__(self, item):
        return self._articles.__getitem__(item)

    def append(self, article):
        self._articles.append(article)

    def reset(self):
        self._articles = []

    def get_articles_not_older_than_days(self, num_days):
        articles_not_older_than_days = []
        for article in self:
            days_from_publication = (datetime.now(timezone.utc).astimezone() - article.published).days
            if num_days >= days_from_publication:
                articles_not_older_than_days.append(article)
        return articles_not_older_than_days