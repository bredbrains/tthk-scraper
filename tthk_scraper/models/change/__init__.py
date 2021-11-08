from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

from tthk_scraper.utils.i18n import ESTONIAN_STATUS_TRIGGERS


class Change(SQLModel, table=True):
    """Change in schedule of lessons"""
    __tablename__ = "changes"
    id: int = Field(default=None, primary_key=True)
    date: datetime
    group: str
    lessons: str
    teacher: str
    room: Optional[str] = None
    status: Optional[str] = None

    def assign_status(self, status_trigger: str):
        lower_status_trigger = status_trigger.lower()
        if lower_status_trigger in ESTONIAN_STATUS_TRIGGERS.keys():
            self.status = ESTONIAN_STATUS_TRIGGERS[lower_status_trigger].value
        else:
            self.room = status_trigger

    def is_equal_with_date(self, date: datetime):
        return self.date.strftime('%Y-%m-%d') == date.strftime('%Y-%m-%d')

