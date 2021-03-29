from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

url = "http://www.yahoo.com"

class DomainCrawler():
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.parsed_starting_url = urlparse(starting_url)
        #print(self.starting_url)
        self.visited_urls = []
        self.processed_pages = 0
        self.max_process_pages = 100

    def start(self):
        self.process_page(self.starting_url)

    def process_page(self, href):
        if self.processed_pages >= self.max_process_pages:
            return
        
        url = urlparse(href)
        if url.netloc == "":
            href = self.parsed_starting_url.scheme + '://' +\
                   self.parsed_starting_url.netloc +\
                   href
        
        if href not in self.visited_urls:
            self.visited_urls.append(href)
        else:
            return

        try:
            response = requests.get(href)
        except:
            return
        
        print('[*] Processing %s' % href)
        self.processed_pages += 1

        soup = BeautifulSoup(response.text,'html.parser')
        
        for link in soup.find_all('a'):
            # process the link to check if it is internal
            if self.is_the_url_internal(link.get('href')):
                self.process_page(link.get('href'))
        

    def is_the_url_internal(self, href):
        url = urlparse(href)
        if url.netloc == "" or url.netloc == self.parsed_starting_url.netloc:
            return True
        else:
            return False

if __name__ == "__main__":
    crawler = DomainCrawler(url)
    crawler.start()

    

