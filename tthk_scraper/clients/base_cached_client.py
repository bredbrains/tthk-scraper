from datetime import datetime

from tthk_scraper.clients.database import BaseDatabaseClient
from tthk_scraper.clients.database.updates_database_client import UpdatesDatabaseClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.api_globals import DEPRECATION_TIME


class BaseCachedClient:
    def __init__(self, model, database_client=None):
        self.model = model
        self.updates_database_client = UpdatesDatabaseClient()
        self.database_client = database_client

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
