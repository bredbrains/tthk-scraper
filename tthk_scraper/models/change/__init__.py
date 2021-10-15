from datetime import datetime

from pydantic import BaseModel

from tthk_scraper.utils.i18n import ESTONIAN_STATUS_TRIGGERS


class Change(BaseModel):
    """Change in schedule of lessons"""
    date: datetime
    group: str
    lessons: str
    teacher: str
    room: str = None
    status: str = None

    def assign_status(self, status_trigger: str):
        lower_status_trigger = status_trigger.lower()
        if lower_status_trigger in ESTONIAN_STATUS_TRIGGERS.keys():
            self.status = ESTONIAN_STATUS_TRIGGERS[lower_status_trigger].value
        else:
            self.room = status_trigger
