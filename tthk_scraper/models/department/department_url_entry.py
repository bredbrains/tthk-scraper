from tthk_scraper.models.department import Department
from tthk_scraper.models.url_entry import UrlEntry


class DepartmentUrlEntry(UrlEntry):
    def __init__(self, department: Department, path: str):
        super().__init__(department.value, path)
