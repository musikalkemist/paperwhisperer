import pytest
from datetime import datetime, timedelta, timezone

from paperwhisperer.retrieval.article import Article
from paperwhisperer.retrieval.searchresults import SearchResults


@pytest.fixture
def search_results():
    return SearchResults("query", "article1", "article2")


def test_search_results_is_instantiated_correctly(search_results):
    assert isinstance(search_results, SearchResults)
    assert search_results.query == "query"
    assert search_results[0] == "article1"
    assert search_results[1] == "article2"


def test_articles_no_older_than_x_days_are_returned():
    article1 = Article("title1", "abstract", ["author"], datetime.now(
        timezone.utc).astimezone() - timedelta(days=9))
    article2 = Article("title2", "abstract", ["author"], datetime.now(
        timezone.utc).astimezone() - timedelta(days=11))
    article3 = Article("title3", "abstract", ["author"], datetime.now(
        timezone.utc).astimezone())
    article4 = Article("title1", "abstract", ["author"], datetime.now(
        timezone.utc).astimezone() - timedelta(days=10))
    search_results = SearchResults("query", article1, article2, article3, article4)
    articles = search_results.get_articles_not_older_than_days(10)
    assert articles == [article1, article3, article4]