from typing import List, Dict

from tthk_scraper.models.department import Department
from tthk_scraper.models.department.department_url_entry import DepartmentUrlEntry
from tthk_scraper.models.url_entry import UrlEntry
from tthk_scraper.utils.blueprints import CHANGES, GROUPS

BASE_URL = "https://www.tthk.ee"

CONSULTATIONS_URLS: List[UrlEntry] = [
    DepartmentUrlEntry(Department.GeneralSubjects, "/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/"),
    DepartmentUrlEntry(Department.Transport,
                       "/oppetoo/opetajate-konsultatsioonid/transporditehnika-valdkonna-konsultatsioonid/"),
    DepartmentUrlEntry(Department.Mechanics,
                       "/oppetoo/opetajate-konsultatsioonid/mehaanika-ja-metallitootluse-valdkonna-konsultatsioonid/"),
    DepartmentUrlEntry(Department.Energy, "/oppetoo/opetajate-konsultatsioonid/mehhatroonka-osakonna-konsultatsiooid/"),
    DepartmentUrlEntry(Department.InformationTechnology, "/infotehnoloogia-valdkonna-konsultatsioonid/"),
    DepartmentUrlEntry(Department.Logistics, "/logistika-valdkonna-konsultatsioonid/"),
    DepartmentUrlEntry(Department.TextileAndSales,
                       "/oppetoo/opetajate-konsultatsioonid/tekstiili-ja-kaubanduse-valdkonna"
                       "-konsultatsioonid/ ")
]

URL_ROUTES: Dict[str, UrlEntry] = {
    CHANGES: UrlEntry("changes", "/tunniplaani-muudatused/"),
    GROUPS: UrlEntry("groups", "/oppetoo/tunniplaan/ruhmajuhatajad/")
}

URLS: Dict[str, str] = {
    CHANGES: BASE_URL + URL_ROUTES[CHANGES].url,
    GROUPS: BASE_URL + URL_ROUTES[GROUPS].url
}
