from typing import List

from tthk_scraper.models.consultation import Consultation
from tthk_scraper.models.department import Department


class Teacher:
    def __init__(self,
                 name: str,
                 room: str,
                 email: str,
                 department: Department,
                 times: List[Consultation]):
        if times is None:
            times = []
        self.name = name
        self.room = room
        self.email = email
        self.department = department
        self.times = times
