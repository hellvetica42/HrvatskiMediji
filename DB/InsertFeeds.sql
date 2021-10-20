INSERT INTO Feed (FeedName, rss, HasContent, mediaID) VALUES
("latest", "https://www.vecernji.hr/feeds/latest", 0, (SELECT rowid FROM Media WHERE MediaName="Vecernji List")),
("", "https://www.jutarnji.hr/feed", 1, (SELECT rowid FROM Media WHERE MediaName="Jutarnji List")),
("news", "https://www.24sata.hr/feeds/news.xml", 0, (SELECT rowid FROM Media WHERE MediaName="24 Sata")),
("", "https://slobodnadalmacija.hr/feed", 0, (SELECT rowid FROM Media WHERE MediaName="Slobodna Dalmacija"));