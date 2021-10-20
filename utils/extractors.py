from utils.Article import Article
import xml.etree.ElementTree as ET
import dateutil.parser as parser
from utils.stripper import strip_html_tags
#functions that extract and create article classes from xml files

#extractor to use when in doubt :)
def default_extractor(xml: str, feedID: int, mediaName: str="") -> list[Article]:
    root = ET.fromstring(xml)

    articles: list[Article] = []

    for item in root[0].findall('item'):

        try:

            title = item.find('title')
            title = "" if title is None else title.text

            link = item.find('link')
            link = "" if link is None else link.text

            description = item.find('description')
            description = "" if description is None else description.text

            if description is not None and len(description) > 0:
                description = strip_html_tags(description)
            else:
                description = ""

            content = item.find('content:encoded')
            content = "" if content is None else content.text

            category = item.find('category')
            category = "" if category is None else category.text

            pubdate = item.find('pubDate')
            pubdate = "" if pubdate is None else pubdate.text
            pubdate = parser.parse(pubdate)
            pubdate = pubdate.isoformat()

        except Exception as e:
            print("Exception while extracting articles from xml")
            print(e)
            continue

        articles.append(Article(mediaName, None, title, description, pubdate, category, link, feedID, content))

    return articles

#extractor that deals with feeds that have no content
def extractor_contentless(xml: str, feedID: int, mediaName: str="") -> list[Article]:
    root = ET.fromstring(xml)

    articles: list[Article] = []

    for item in root[0].findall('item'):

        try:

            title = item.find('title')
            title = "" if title is None else title.text

            link = item.find('link')
            link = "" if link is None else link.text

            description = item.find('description')
            description = "" if description is None else description.text

            if description is not None and len(description) > 0:
                description = strip_html_tags(description)
            else:
                description = ""

            category = item.find('category')
            category = "" if category is None else category.text

            pubdate = item.find('pubDate')
            pubdate = "" if pubdate is None else pubdate.text
            pubdate = parser.parse(pubdate)
            pubdate = pubdate.isoformat()

        except Exception as e:
            print("Exception while extracting articles from xml")
            print(e)
            continue

        articles.append(Article(mediaName, None, title, description, pubdate, category, link, feedID))

    return articles


