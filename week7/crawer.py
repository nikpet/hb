import requests
from bs4 import BeautifulSoup
import re
from histogram import Histogram
import json
# import socket


class Crawer:
    def __init__(self):
        self.links = []
        self.servers = Histogram()
        self.uri = 'http://register.start.bg/'
        self.our_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        request = requests.get("http://register.start.bg",
                               headers=self.our_headers)
        soup = BeautifulSoup(request.text)
        for link in soup.find_all(href=re.compile('link.php')):
            self.links.append(link.get('href'))

    def craw(self):
        for link in self.links:
            new_url = requests.head(self.uri + link,
                                    headers=self.our_headers).headers['Location']
            try:
                server = requests.head(new_url, timeout=2,
                                       headers=self.our_headers).headers['server']
                server = self.clean(server)
                self.servers.add(server)
            # except requests.exceptions.RequestException:
            #     pass
            # except KeyError:
            #     pass
            # except socket.timeout:
            #     pass
            except Exception:
                pass
        self.save()

    def clean(self, server_name):
        clean_server = server_name
        if '/' in server_name:
            clean_server = server_name[0:server_name.index('/')]
        return clean_server


if __name__ == '__main__':
    c = Crawer()
    c.craw()
    c.save()
