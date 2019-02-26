from flask import Flask, render_template, request, jsonify
from utils import get_url, get_summary
from constants import HOST
app = Flask(__name__)


@app.route('/')
def index():
    """
    loads the index page
    :return:
    """
    return render_template("inp.html",host=HOST)


@app.route('/summary')
def summary():
    """
    :param URL: URL to take the text from
    :return: summary of the page in json format.
    """
    url = request.args.get("url")
    page = get_url(url)
    return jsonify(get_summary(page))


if __name__ == '__main__':
    app.run(debug=True)
