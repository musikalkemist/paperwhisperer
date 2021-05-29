from datetime import datetime

from paperwhisperer.retrieval.article import Article


def test_article_is_instantiated_correctly():
    article = Article("title", "abstract", ["author1", "author2"],
                      datetime.now())
    assert article.title == "title"
    assert article.abstract == "abstract"
    assert article.authors == ["author1", "author2"]
    assert isinstance(article.published, datetime)


def test_description_is_returned_correctly():
    article = Article("An interesting title",
                      "An abstract",
                      ["author 1", "author2"],
                      datetime.now())
    assert article.description == "Title: An interesting title. Authors: " \
                                  "author 1, author2. Abstract: An abstract"