from tthk_scraper.clients.base_cached_client import BaseCachedClient
from tthk_scraper.clients.parsers.teachers_parser_client import TeachersParserClient
from tthk_scraper.models.teacher import Teacher
from tthk_scraper.services.teacher_service import TeacherService
from tthk_scraper.utils.urls import CONSULTATIONS_URLS


class TeachersClient(BaseCachedClient):
    def __init__(self):
        super().__init__(Teacher, TeachersParserClient(), TeacherService(), CONSULTATIONS_URLS)
