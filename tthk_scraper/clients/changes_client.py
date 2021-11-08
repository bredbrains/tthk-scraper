from datetime import datetime
from typing import List

from tthk_scraper.clients.base_cached_client import BaseCachedClient
from tthk_scraper.clients.browser_client import BrowserClient
from tthk_scraper.clients.database.changes_database_client import ChangesDatabaseClient
from tthk_scraper.clients.database.updates_database_client import UpdatesDatabaseClient
from tthk_scraper.clients.parsers.changes_parser_client import ChangesParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.blueprints import CHANGES
from tthk_scraper.utils.urls import URLS


class ChangesClient(BaseCachedClient):
    def __init__(self):
        super().__init__(Change, ChangesDatabaseClient())
        self.url = URLS[CHANGES]

    def get_changes(self) -> List[Change]:
        changes = self.database_client.get_all()
        is_deprecated = self.is_deprecated()
        if len(changes) == 0 or is_deprecated:
            return self.get_new_changes(is_deprecated)
        return changes

    def get_changes_by_date(self, received_date: str) -> List[Change]:
        changes = self.get_changes()
        date = datetime.strptime(received_date, '%Y-%m-%d')
        return ChangesClient.filter_changes_by_date(changes, date)

    def get_new_changes(self, is_deprecated: bool = False):
        document = BrowserClient(self.url).open_page()
        changes = ChangesParserClient(document).parse()
        table = Change.__tablename__
        self.updates_database_client.save_update_time(table)
        self.database_client.update(changes) if is_deprecated else self.database_client.save(changes)
        return changes

    @staticmethod
    def filter_changes_by_date(changes: List[Change], date: datetime) -> List[Change]:
        filtered_changes = filter(lambda change: change.is_equal_with_date(date), changes)
        return list(filtered_changes)
