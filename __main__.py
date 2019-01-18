from flask import Flask, render_template, request, jsonify
import textSummarizer as ts
import json
import sqlite3 as lite
import feedparser
from newspaper import Article
from nltk.tokenize import sent_tokenize
from operator import itemgetter
from nltk.corpus import brown, stopwords
import warnings
import csv
app = Flask(__name__, template_folder='templates')

@app.route('/inp')
def summary():
    return render_template("inp.html")

@app.route('/out', methods=['POST', 'GET'])
def out():
    if request.method == 'POST':
        out = request.form
        d={}
        for k,v in out.items():
            d[k]=v
        url= d['URL']
        l = url.split('.')
        name = l[1]
        article = Article(url, language='en')
        article.download()
        article.parse()
        article_content = article.text
        article_title = article.title

        warnings.filterwarnings('ignore')



        stop_words = stopwords.words('english')

        counter = 0
        temp = ""
        con = lite.connect('paperstuff.db')
        with con:
            cur = con.cursor()
            sentences = sent_tokenize(article_content)
            S = ts.build_similarity_matrix(sentences, stop_words)
            sentence_ranks = ts.pagerank(S)
            ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
            SUMMARY_SIZE = 4
            SELECTED_SENTENCES = sorted(ranked_sentence_indexes[:SUMMARY_SIZE])
            summary = itemgetter(*SELECTED_SENTENCES)(sentences)
            temp=''
            for sentence in summary:
                temp+=''.join(sentence)
                cur.execute("INSERT INTO Paper VALUES(?,?,?)",(name.encode(), article_title.encode(), temp.encode()))
                counter+=1

        return jsonify({'summary':temp})

if __name__ == '__main__':
    app.run(debug = True)
