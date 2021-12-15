from datetime import datetime
from typing import List

from tthk_scraper.clients.base_singular_cached_client import BaseSingularCachedClient
from tthk_scraper.clients.parsers.changes_parser_client import ChangesParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.services.change_service import ChangeService
from tthk_scraper.utils.blueprints import CHANGES
from tthk_scraper.utils.urls import URLS


class ChangesClient(BaseSingularCachedClient):
    def __init__(self):
        super().__init__(Change, ChangesParserClient(), ChangeService(), URLS[CHANGES])

    def get_by_date(self, received_date: str) -> List[Change]:
        changes = self.get()
        date = datetime.strptime(received_date, '%Y-%m-%d')
        return ChangesClient.filter_changes_by_date(changes, date)

    @staticmethod
    def filter_changes_by_date(changes: List[Change], date: datetime) -> List[Change]:
        filtered_changes = filter(lambda change: change.is_equal_with_date(date), changes)
        return list(filtered_changes)
