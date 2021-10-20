import sqlite3

from utils.Article import Article

def insertArticles(articles: list[Article], cur: sqlite3.Cursor):
    #db format for Article table is: (Title, Description, Content, Date, Link, Hash)
    tpls: list[tuple] = [a.getTupleFormat() for a in articles]

    query = """INSERT OR IGNORE INTO Article(Title, Description, Content, Date, Link, Hash) VALUES(?, ?, ?, ?, ?, ?);"""

    print("Inserting rows into Article")
    cur.executemany(query, tpls)
    print("Inserted", cur.rowcount, "rows")

    if cur.rowcount == 0:
        print("No rows inserted, returning")
        return

    #Get article ids using hashes
    print("Getting row ids using hashes")
    hashes = [t[-1] for t in tpls]

    query = f"""SELECT articleID, Hash FROM Article WHERE Hash in ({','.join(['?']*len(hashes))})"""
    cur.execute(query, hashes)
    #[ (articleID, Hash) ]
    idHashPairs = cur.fetchall()
    print("Got", len(idHashPairs), "pairs.")

    #Connecting article ids with feed ids from article list
    # {hash : feedID}
    hashToFeedId = {a.hash : a.feedId for a in articles}

    # {feedID, articleID}
    idIdPairs = [(hashToFeedId[h[1]], h[0]) for h in idHashPairs]

    #Connect feeds and articles
    #insert into many to many From Feed table 

    query = f"""INSERT OR IGNORE INTO From_Feed(feedID, articleID) VALUES (?, ?);"""
    print("Inserting rows into From_Feed table")
    cur.executemany(query, idIdPairs)
    print("Inserted", cur.rowcount, "Rows")

    # Insert new categories into category Table
    categories = {a.category for a in articles if len(a.category) > 0}
    categories = [(c,) for c in categories]
    query = f"""INSERT OR IGNORE INTO Category(CategoryName) VALUES (?);"""
    print("Inserting new categories")
    cur.executemany(query, categories)
    print("Inserted", cur.rowcount, "new categories")

    #Connect articles and categories
    query = f"""SELECT categoryID, CategoryName FROM Category"""
    cur.execute(query)
    categoryNameIDPairs = cur.fetchall()
    #category id pair {CategoryName : categoryID}
    categoryNameIDPairs = {c[1] : c[0] for c in categoryNameIDPairs}

    # {articleHash : articleID}
    hashToArticleID = {a[1] : a[0] for a in idHashPairs}

    #(articleID, categoryID)
    inCategoryPairs = [(hashToArticleID[a.hash], categoryNameIDPairs[a.category]) for a in articles if len(a.category) > 0]

    query = f"""INSERT OR IGNORE INTO In_category(articleID, categoryID) VALUES (?,?);"""
    print("Inserting rows into In_category table")
    cur.executemany(query, inCategoryPairs)
    print("Inserted", cur.rowcount, "Rows")

