import requests
from bs4 import BeautifulSoup


class BrowserClient:
    def __init__(self, url):
        self.url = url

    def open_page(self) -> BeautifulSoup:
        response = requests.get(self.url)
        document = BeautifulSoup(response.text, 'html.parser')
        return document
