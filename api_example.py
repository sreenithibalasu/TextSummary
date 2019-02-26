import requests

"""
API example for summarizer
URL - constant server URL
request_url - Page that needs to be parsed and summarized.
"""

URL = "http://localhost:5000/summary"
request_url = "https://nvie.com/posts/writing-a-cli-in-python-in-under-60-seconds/"
r = requests.get(URL + "?url=" + request_url)
print(r.json())
