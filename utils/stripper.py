import re

def strip_html_tags(data: str) -> str:
    try:
        p = re.compile(r'<.*?>')
        return p.sub('', data)

    except Exception as e:
        print("Exception while stripping html tags")
        print(e)
        return data
    