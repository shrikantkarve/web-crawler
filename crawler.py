import requests
import re


class PyCrawler(object):
    def init(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()

    def start(self):
        pass


if __name__ == "__main__":
    crawler = PyCrawler()
    crawler.start()
