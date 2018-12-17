import json

data = {
    "content": [
        {
            "name": "The Hindu Business Line",
            "url": "https://www.thehindubusinessline.com/news/national/feeder/default.rss"
        },
        {
            "name": "Financial Express",
            "url": "https://www.financialexpress.com/feed/"
        }
    ]
}

#Write data into json
with open("test2.json", "w") as write_file:
    json.dump(data, write_file)
