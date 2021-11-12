from datetime import datetime

from sqlmodel import select

from tthk_scraper.services import BaseService
from tthk_scraper.models.update_time import UpdateTime


class UpdateService(BaseService):
    def __init__(self):
        super().__init__(UpdateTime)

    def get_by_table(self, table: str) -> UpdateTime:
        statement = select(UpdateTime).where(UpdateTime.table == table)
        update_time = self.session.exec(statement).first()
        return update_time

    def save(self, table: str):
        update_time = self.get_by_table(table)
        current_time = datetime.now()
        if update_time is None:
            update_time = UpdateTime(table=table, timestamp=current_time)
            self.session.add(update_time)
        else:
            update_time.timestamp = current_time
            self.session.add(update_time)
        self.session.commit()
