import argparse
from pathlib import Path

from paperwhisperer.retrieval.arxivretriever import ArxivRetriever
from paperwhisperer.retrieval.pubmedretriever import PubmedRetriever
from paperwhisperer.tts.ttsprocessor import TTSProcessor
from paperwhisperer.tts.googlespeechynthesiser import GoogleSpeechSynthesiser


def create_summaries():
    """The "create_summaries" entry point:
        1. retrieves relevant articles from arXiv based on a keyword search,
        2. uses the Google Cloud Text-To-Speech to synthesise a summary of
        the articles,
        3. stores the vocal summary on disk

    Sample usage:

    $ create_summaries "music generation deep learning" 20 /home/valerio/summaries/today/1 30

    Script positional arguments:
        - query: keywords used for searching articles
        - max_articles: maximum number of articles to retrieve
        - save_dir: directory where to store vocal summaries
        - num_days: retrieve articles no older than this value in days
    """
    query, max_articles, save_dir, num_days = _parse_console_arguments()
    _process_summaries(query, max_articles, save_dir, num_days)


def _process_summaries(query, max_articles, save_dir, num_days):
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    arxiv_retriever, pubmed_retriever, tts_processor = _create_objects(query,
                                                                       max_articles,
                                                                       save_dir)
    search_results = arxiv_retriever.get_articles()
    search_results_pubmed = pubmed_retriever.get_articles()

    for pubmed_result in search_results_pubmed:
        search_results.append(pubmed_result)

    articles = search_results.get_articles_not_older_than_days(num_days)
    if articles:
        tts_processor.synthesise_and_save(articles)
    else:
        print(f"There are no articles for query '{query}' which have been "
              f"published {num_days} days ago or less.")


def _parse_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("query",
                        help="keywords used for searching articles",
                        type=str)
    parser.add_argument("max_articles",
                        help="maximum number of articles to retrieve",
                        type=int)
    parser.add_argument("save_dir",
                        help="directory where to store summaries",
                        type=str)
    parser.add_argument("num_days",
                        help="retrieve articles no older than this value in "
                             "days",
                        type=int)
    args = parser.parse_args()
    return args.query, args.max_articles, args.save_dir, args.num_days


def _create_objects(query, max_results, save_dir):
    arxiv_retriever = ArxivRetriever(query, max_results)
    pubmed_retriever = PubmedRetriever(query, max_results)
    speech_synthesiser = GoogleSpeechSynthesiser()
    tts_processor = TTSProcessor(speech_synthesiser, save_dir)
    return arxiv_retriever, pubmed_retriever, tts_processor
