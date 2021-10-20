CREATE TABLE Media
(
  mediaID INTEGER PRIMARY KEY,
  MediaName TEXT NOT NULL,
  Link TEXT NOT NULL
);

CREATE TABLE Feed
(
  feedID INTEGER PRIMARY KEY,
  FeedName TEXT,
  rss TEXT NOT NULL,
  HasContent INTEGER NOT NULL,
  mediaID INTEGER NOT NULL,
  FOREIGN KEY (mediaID) REFERENCES Media(mediaID)
);

CREATE TABLE Article
(
  articleID INTEGER PRIMARY KEY,
  Title TEXT NOT NULL,
  Description TEXT NOT NULL,
  Content TEXT,
  Date TEXT,
  Link TEXT,
  Hash TEXT NOT NULL,
  UNIQUE(Hash)
);

CREATE TABLE Author
(
  authorID INTEGER PRIMARY KEY,
  Name TEXT NOT NULL
);

CREATE TABLE Category
(
  categoryID INTEGER PRIMARY KEY,
  CategoryName TEXT NOT NULL,
  UNIQUE(CategoryName)
);

CREATE TABLE From_Feed
(
  feedID INTEGER NOT NULL,
  articleID INTEGER NOT NULL,
  PRIMARY KEY (feedID, articleID),
  FOREIGN KEY (feedID) REFERENCES Feed(feedID) ON DELETE CASCADE,
  FOREIGN KEY (articleID) REFERENCES Article(articleID) ON DELETE CASCADE
);

CREATE TABLE Works_For
(
  authorID INTEGER NOT NULL,
  mediaID INTEGER NOT NULL,
  PRIMARY KEY (authorID, mediaID),
  FOREIGN KEY (authorID) REFERENCES Author(authorID),
  FOREIGN KEY (mediaID) REFERENCES Media(mediaID)
);

CREATE TABLE In_category
(
  articleID INTEGER NOT NULL,
  categoryID INTEGER NOT NULL,
  PRIMARY KEY (articleID, categoryID),
  FOREIGN KEY (articleID) REFERENCES Article(articleID) ON DELETE CASCADE,
  FOREIGN KEY (categoryID) REFERENCES Category(categoryID) ON DELETE CASCADE
);

CREATE TABLE Wrote_Article
(
  authorID INTEGER NOT NULL,
  articleID INTEGER NOT NULL,
  PRIMARY KEY (authorID, articleID),
  FOREIGN KEY (authorID) REFERENCES Author(authorID),
  FOREIGN KEY (articleID) REFERENCES Article(articleID)
);