from typing import List

from sqlmodel import select

from tthk_scraper.clients.database import BaseDatabaseClient
from tthk_scraper.models.change import Change


class ChangesDatabaseClient(BaseDatabaseClient):
    def __init__(self):
        super().__init__(Change)

