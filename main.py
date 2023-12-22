import feedparser
import json

def parse_rss(url):
    news = feedparser.parse(url)
    posts = []

    for post in news.entries:
        posts.append({
            "title": post.title,
            "description": post.description,
            "publication_date": post.published,
            "link": post.link
        })

    return posts


def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


rss_url = "http://rss.cnn.com/rss/cnn_latest.rss"
news_data = parse_rss(rss_url)

json_filename = "CNN_data.json"
save_as_json(news_data, json_filename)