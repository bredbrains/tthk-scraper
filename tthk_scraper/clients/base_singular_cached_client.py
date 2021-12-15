from abc import ABC
from typing import Type

from sqlmodel import SQLModel

from tthk_scraper.clients.base_cached_client import BaseCachedClient
from tthk_scraper.clients.parsers.base_parser_client import BaseParserClient
from tthk_scraper.services import BaseService


class BaseSingularCachedClient(BaseCachedClient, ABC):
    def __init__(self, model: Type[SQLModel], parser_client: BaseParserClient, service: BaseService, url: str):
        super().__init__(model, parser_client, service, [url])

    def get(self):
        data = self.service.get_all()
        is_deprecated = self.is_deprecated()
        is_first = True
        if len(data) == 0 or is_deprecated:
            return self.fetch_remote_data(self.urls[0], is_deprecated, is_first)
        return data
