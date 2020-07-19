from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/tables"

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

if __name__ == "__main__":
    #r = requests.get(url)
    #data = r.text
    #soup = BeautifulSoup(data,'html.parser')
    soup = BeautifulSoup(html_doc,'html.parser')
    print(soup.prettify)
    l = []
    for link in soup.find_all('a'):
        l.append(link.get('class'))
    
    for i in l:
        print(i)

