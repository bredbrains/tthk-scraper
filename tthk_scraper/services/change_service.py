from tthk_scraper.services import BaseService
from tthk_scraper.models.change import Change


class ChangeService(BaseService):
    def __init__(self):
        super().__init__(Change)

