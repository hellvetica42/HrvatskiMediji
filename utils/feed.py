from typing import Callable
import xml.etree.ElementTree as ET
import requests

from utils.Article import Article


#get all the info from list of rss feeds (feed ID, feed link, media name, extractor function)
def collectFeeds(feedList: list[tuple[int, str, str, Callable[[str, str, str], list[Article]] ]]) -> list[Article]:
    articles: list[Article]= []
    feedArticles = []

    for feed in feedList:
        feedID, rss, mediaName, extractor = feed
        
        try:
            r = requests.get(rss, allow_redirects=True)

        except Exception as e:
            print("Getting rss feed", feedID, "from media", mediaName, "using feed", rss, "failed")
            print(e)
            continue

        feedArticles = extractor(r.content, feedID, mediaName)

        articles.extend(feedArticles)

    return articles