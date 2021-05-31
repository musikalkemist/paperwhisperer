from pymed import PubMed
import os
from datetime import datetime

from paperwhisperer.retrieval.article import Article
from paperwhisperer.retrieval.searchresults import SearchResults


class PubmedRetriever:
    """PubmedRetriever is responsible to place a call to the PubMed API and
    retrieve articles' metadata. To place the call the class uses the
    'pymed' library.

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

    def get_articles(self):
        """Retrieve articles from pubmed placing an API call via the pymed
        package. We need to give a tool name(any) and a valid email to pubmed for
        using their apis. Mention this in config.env file 

        :return: (SearchResults) Sequence of articles retrieved from pubmed
        """
        pubmed = PubMed(tool=os.environ.get('PUBMED_TOOL'),
                        email=os.environ.get('PUBMED_EMAIL'))
        query_results = pubmed.query(self._query, max_results=self.max_results)
        search_results = self._to_search_results(query_results)
        return search_results

    def _to_search_results(self, query_results):
        search_results = SearchResults(self.query)
        authors = []
        for query_result in query_results:
            for author in query_result.authors:
                if(author['firstname'] != None and author['lastname'] != None):
                    authors.append(author['firstname']+' '+author['lastname'])
                elif(author['firstname'] == None and author['lastname'] != None):
                    authors.append(author['lastname'])
                elif(author['firstname'] != None and author['lastname'] == None):
                    authors.append(author['firstname'])
                else:
                    authors.append('unknown')

            midnight_time = datetime.min.time()
            publication_date = datetime.combine(
                query_result.publication_date, midnight_time).astimezone()

            article = Article(query_result.title,
                              query_result.abstract,
                              authors,
                              publication_date)
            search_results.append(article)
        return search_results
