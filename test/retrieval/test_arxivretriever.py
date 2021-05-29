import pytest

from paperwhisperer.retrieval.arxivretriever import ArxivRetriever
from paperwhisperer.retrieval.searchresults import SearchResults
from paperwhisperer.retrieval.article import Article


@pytest.fixture
def arxivretriever():
    return ArxivRetriever("melody generation deep learning", 5)


def test_arxiv_retriever_is_instantiated_correctly(arxivretriever):
    assert isinstance(arxivretriever, ArxivRetriever)
    assert arxivretriever.query == "melody generation deep learning"
    assert arxivretriever._arxiv_query == "melody AND generation AND deep AND learning"
    assert arxivretriever.max_results == 5


def test_set_arxiv_query(arxivretriever):
    arxivretriever._set_arxiv_query("singlewordquery")
    assert arxivretriever._arxiv_query == "singlewordquery"

    arxivretriever._set_arxiv_query("multiple word query")
    assert arxivretriever._arxiv_query == "multiple AND word AND query"


def test_articles_are_retrieved(arxivretriever):
    search_results = arxivretriever.get_articles()
    assert isinstance(search_results, SearchResults)
    assert len(search_results) == 5
    assert isinstance(search_results[0], Article)
    assert isinstance(search_results[0].authors[0], str)