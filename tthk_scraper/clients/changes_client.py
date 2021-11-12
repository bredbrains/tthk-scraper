from datetime import datetime
from typing import List

from tthk_scraper.clients.base_cached_client import BaseCachedClient
from tthk_scraper.clients.database.changes_database_client import ChangesDatabaseClient
from tthk_scraper.clients.parsers.changes_parser_client import ChangesParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.blueprints import CHANGES
from tthk_scraper.utils.urls import URLS


class ChangesClient(BaseCachedClient):
    def __init__(self):
        super().__init__(Change, URLS[CHANGES], ChangesParserClient(), ChangesDatabaseClient())

    def get_by_date(self, received_date: str) -> List[Change]:
        changes = self.get()
        date = datetime.strptime(received_date, '%Y-%m-%d')
        return ChangesClient.filter_changes_by_date(changes, date)

    @staticmethod
    def filter_changes_by_date(changes: List[Change], date: datetime) -> List[Change]:
        filtered_changes = filter(lambda change: change.is_equal_with_date(date), changes)
        return list(filtered_changes)
