import requests
from bs4 import BeautifulSoup
import re


class Crawer:
    def __init__(self):
        self.links = []
        self.browsers = []
        self.uri = 'http://register.start.bg/'
        self.our_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        request = requests.get("http://register.start.bg", headers=self.our_headers)
        soup = BeautifulSoup(request.text)
        for link in soup.find_all(href=re.compile('link.php'), limit=1):
            self.links.append(link.get('href'))

    def craw(self):
        for link in self.links:
            self.browsers.append(requests.head(self.uri + link, headers=self.our_headers).headers['Server'])
        return self.browsers


if __name__ == '__main__':
    c = Crawer()
    print(c.craw())
