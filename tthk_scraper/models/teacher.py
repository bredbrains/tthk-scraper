from typing import List, Any

from sqlmodel import SQLModel

from tthk_scraper.models.department import Consultation
from tthk_scraper.models.department import Department


class Teacher(SQLModel):
    def __init__(self, name: str, room: str, email: str, department: Department, times: List[Consultation],
                 **data: Any):
        super().__init__(**data)
        if times is None:
            times = []
        self.name = name
        self.room = room
        self.email = email
        self.department = department
        self.times = times
