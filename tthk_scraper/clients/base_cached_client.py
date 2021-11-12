from datetime import datetime
from typing import Type

from sqlmodel import SQLModel

from tthk_scraper.clients.browser_client import BrowserClient
from tthk_scraper.clients.database import BaseDatabaseClient
from tthk_scraper.clients.database.updates_database_client import UpdatesDatabaseClient
from tthk_scraper.clients.parsers.base_parser_client import BaseParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.api_globals import DEPRECATION_TIME


class BaseCachedClient:
    def __init__(self, model: Type[SQLModel],
                 url: str,
                 parser_client: BaseParserClient,
                 database_client: BaseDatabaseClient):
        self.model = model
        self.url = url
        self.database_client = database_client
        self.parser_client = parser_client
        self.updates_database_client = UpdatesDatabaseClient()

    def get(self):
        data = self.database_client.get_all()
        is_deprecated = self.is_deprecated()
        if len(data) == 0 or is_deprecated:
            return self.get_new(is_deprecated)
        return data

    def get_new(self, is_deprecated: bool = False):
        document = BrowserClient(self.url).open_page()
        data = self.parser_client.parse(document)
        self.updates_database_client.save(self.model.__tablename__)
        self.database_client.update(data) if is_deprecated else self.database_client.save(data)
        return data

    def is_deprecated(self):
        table = self.model.__tablename__
        update_time = self.updates_database_client.get_by_table(table)
        if update_time is None:
            return True
        current_time = datetime.now()
        update_diff = current_time - update_time.timestamp
        return update_diff.total_seconds() / 3600 > DEPRECATION_TIME[table]

    def save(self, models):
        self.database_client.save(models)
