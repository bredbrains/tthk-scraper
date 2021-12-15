from abc import ABC
from datetime import datetime
from typing import Type, List

from sqlmodel import SQLModel

from tthk_scraper.clients.browser_client import BrowserClient
from tthk_scraper.clients.parsers.base_parser_client import BaseParserClient
from tthk_scraper.services import BaseService
from tthk_scraper.services.update_service import UpdateService
from tthk_scraper.utils.api_globals import DEPRECATION_TIME


class BaseCachedClient(ABC):
    def __init__(self,
                 model: Type[SQLModel],
                 parser_client: BaseParserClient,
                 service: BaseService,
                 urls: List[str]):
        self.model = model
        self.urls = urls
        self.service = service
        self.parser_client = parser_client
        self.updates_database_client = UpdateService()

    @property
    def tablename(self):
        return self.model.__tablename__

    def get(self):
        data = self.service.get_all()
        is_deprecated = self.is_deprecated()
        if len(data) == 0 or is_deprecated:
            data = []
            for index, url in enumerate(self.urls):
                is_first = index == 0
                data += self.fetch_remote_data(url, is_deprecated, is_first)
            return data
        return data

    def fetch_remote_data(self, url: str, is_deprecated: bool = False, is_first: bool = False):
        document = BrowserClient(url).open_page()
        data = self.parser_client.parse(document)
        if is_first:
            self.updates_database_client.save(self.tablename)
        self.service.update(data, is_first) if is_deprecated else self.service.save(data)
        return data

    def is_deprecated(self):
        update_time = self.updates_database_client.get_by_table(self.tablename)
        if update_time is None:
            return True
        current_time = datetime.now()
        update_diff = current_time - update_time.timestamp
        return update_diff.total_seconds() / 3600 > DEPRECATION_TIME[self.tablename]

    def save(self, models):
        self.service.save(models)
