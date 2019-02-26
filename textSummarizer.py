import numpy as np
from nltk.tokenize import sent_tokenize
from operator import itemgetter
from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
import warnings

warnings.filterwarnings('ignore')
stop_words = stopwords.words('english')


def sentence_similarity(sent1, sent2, stopwords=None):
    """
    returns the sentence similarity between two given sentences
    :param sent1: sentence 1 - string
    :param sent2: sentence 2 - string
    :param stopwords: A list of english stop words
    :return:
    """
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stopwords=None):
    # Create an empty similarity matrix
    S = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue

            S[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    # normalize the matrix row-wise

    for idx in range(len(S)):
        if (S[idx].sum() == 0):
            break
        S[idx] /= S[idx].sum()

    return S


def pagerank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P
