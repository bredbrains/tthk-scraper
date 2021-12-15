from tthk_scraper.models.teacher import Teacher
from tthk_scraper.services import BaseService


class TeacherService(BaseService):
    def __init__(self):
        super().__init__(Teacher)

