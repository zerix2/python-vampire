#!/home/mcdade1/anaconda3/bin/python3

"""
Another script to wrap my head around lxml and scraping. 
"""

import requests
import lxml
from lxml import html

link = 'http://d6holocron.com/wiki/index.php?title=A-wing'
headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'}
page = requests.get(link, headers=headers)
tree = html.document_fromstring(page.content)

tableinfo = tree.cssselect("[id=mw-content-text]")

for item in tableinfo:
    print(item.text_content())