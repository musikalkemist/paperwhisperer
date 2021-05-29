from arxiv import Search, SortCriterion

from paperwhisperer.retrieval.article import Article
from paperwhisperer.retrieval.searchresults import SearchResults


class ArxivRetriever:
    """ArxivRetriever is responsible to place a call to the arxiv API and
    retrieve articles' metadata. To place the call the class uses the
    'arxiv' library.

    Attrs:
        - query (str): Search query
        - max_results: Max number of results
    """

    def __init__(self, query, max_results):
        self.query = query
        self.max_results = max_results

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, query):
        self._query = query
        self._set_arxiv_query(query)

    def get_articles(self):
        """Retrieve articles from arxiv placing an API call via the arxiv
        package.

        :return: (SearchResults) Sequence of articles retrieved from arxiv
        """
        query_results = Search(query=self._arxiv_query,
                               max_results=self.max_results,
                               sort_by=SortCriterion.SubmittedDate).get()
        search_results = self._to_search_results(query_results)
        return search_results

    def _to_search_results(self, query_results):
        search_results = SearchResults(self.query)
        for query_result in query_results:
            authors = [author.name for author in query_result.authors]
            article = Article(query_result.title,
                              query_result.summary,
                              authors,
                              query_result.updated)
            search_results.append(article)
        return search_results

    def _set_arxiv_query(self, query):
        words_in_query = query.split()
        if len(words_in_query) > 1:
            self._arxiv_query = " AND ".join(words_in_query)
        else:
            self._arxiv_query = query