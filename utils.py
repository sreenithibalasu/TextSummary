import textSummarizer as ts
from newspaper import Article
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from operator import itemgetter


def get_url(url):
    """
    parses the url using newspaper3k
    :param url: URL for the page
    :return: dict(title,content)
    """
    article = Article(url, language='en')
    article.download()
    article.parse()
    return {"title": article.title, "text": article.text}


def get_summary(page):
    """
    get the summary of the content given
    :param page: dict(title,text)
    :return: summary
    """
    stop_words = stopwords.words('english')
    sentences = sent_tokenize(page["text"])
    S = ts.build_similarity_matrix(sentences, stop_words)
    sentence_ranks = ts.pagerank(S)
    ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
    SUMMARY_SIZE = 4
    SELECTED_SENTENCES = sorted(ranked_sentence_indexes[:SUMMARY_SIZE])
    summary = itemgetter(*SELECTED_SENTENCES)(sentences)
    temp = ''
    for sentence in summary:
        temp += ''.join(sentence)
    return {"summary": temp}
