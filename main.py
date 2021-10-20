#main file that collects all feeds and stores them in db
from utils.insertArticle import insertArticles
from utils.extractors import extractor_contentless, default_extractor
from utils.feed import collectFeeds
from utils.Article import Article

import sqlite3
_DB_PATH = 'DB/data.db'

if __name__ == "__main__":
    db = sqlite3.connect(_DB_PATH)
    cur = db.cursor()

    feeds = []
    #gets feeds from db
    for row in cur.execute("""SELECT feedID, rss, HasContent, MediaName 
                            FROM Feed INNER JOIN Media USING(mediaID)"""):

        if row[2] == 1:
            fn = default_extractor
        else:
            fn = extractor_contentless

        #(feed name, feed link, media name, extractor function)
        feeds.append((row[0], row[1], row[3], fn))

    articles: list[Article] = collectFeeds(feeds)
    insertArticles(articles, cur)

    db.commit()

        