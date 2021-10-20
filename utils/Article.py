import hashlib

class Article:
    def __init__(self, media, author, title, description, date, category, link, feedId, content=""):
        self.media = media
        self.author = author
        self.title = title
        self.description = description
        self.date = date
        self.category = category
        self.content = content
        self.link = link
        self.feedId = feedId

        self.hash = hashlib.md5((self.title + self.description + self.date).encode('utf-8')).hexdigest()

    def __str__(self) -> str:
        outstr = f"""
        MediaName: {self.media}\n
        Title: {self.title}\n
        Category: {self.category}\n
        Description: {self.description}\n
        """

        return outstr

    '''
    def __repr__(self) -> str:
        outstr = f"""
        MediaName: {self.media}\n
        Title: {self.title}\n
        Date: {self.date}\n
        Category: {self.category}\n
        Link: {self.link}\n
        Description: {self.description}\n
        """

        return outstr
    '''

    def getTupleFormat(self):
        #db format for Article table is: (Title, Description, Content, Date, Link, Hash)
        tpl = (self.title, self.description, self.content, self.date, self.link, self.hash)
        return tpl
