import requests
from bs4 import BeautifulSoup
import re
from histogram import Histogram
import sqlite3
# import socket


class Crawer:
    def __init__(self):
        self.links = []
        self.servers = Histogram()
        self.uri = 'http://register.start.bg/'
        self.our_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        self.db = sqlite3.connect('base.sqlite3')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self._init_db()
        request = requests.get("http://register.start.bg",
                               headers=self.our_headers)
        soup = BeautifulSoup(request.text)
        for link in soup.find_all(href=re.compile('link.php')):
            self.links.append(link.get('href'))

    def _init_db(self):
        create_table = """
            CREATE TABLE IF NOT EXISTS servers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            count INTEGER,
            )
            """
            self.cursor.execute(create_table)

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
        self.save(server)

    def clean(self, server_name):
        clean_server = server_name
        if '/' in server_name:
            clean_server = server_name[0:server_name.index('/')]
        return clean_server

    def save(self, data):
        query = """
            INSERT INTO servers
            (name, count)
            VALUES (:name, :count)
            """
        self.cursor.execute(query, data)
        return self.cursor.lastrowid


    @staticmethod
    def load():
        with open(file_name, 'r') as fd:
            hist = Histogram()
            hist.vault = json.load(fd)
        return hist


if __name__ == '__main__':
    c = Crawer()
    c.craw()
    c.save()
