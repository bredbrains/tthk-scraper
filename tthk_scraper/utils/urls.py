from tthk_scraper.models.department import Department
from tthk_scraper.utils.blueprints import CHANGES, GROUPS, CONSULTATIONS

BASE_URL = "https://www.tthk.ee"

CONSULTATIONS_URLS = {
    Department.GeneralSubjects: "/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/",
    Department.Transport: "/oppetoo/opetajate-konsultatsioonid/transporditehnika-valdkonna-konsultatsioonid/",
    Department.Mechanics: "/oppetoo/opetajate-konsultatsioonid/mehaanika-ja-metallitootluse-valdkonna-konsultatsioonid/",
    Department.Energy: "/oppetoo/opetajate-konsultatsioonid/mehhatroonka-osakonna-konsultatsiooid/",
    Department.InformationTechnology: "/infotehnoloogia-valdkonna-konsultatsioonid/",
    Department.Logistics: "/logistika-valdkonna-konsultatsioonid/",
    Department.TextileAndSales: "/oppetoo/opetajate-konsultatsioonid/tekstiili-ja-kaubanduse-valdkonna"
                                "-konsultatsioonid/ "
}

URL_ROUTES = {
    CHANGES: "/tunniplaani-muudatused/",
    GROUPS: "/oppetoo/tunniplaan/ruhmajuhatajad/",
    CONSULTATIONS: CONSULTATIONS_URLS
}

URLS = {
    CHANGES: BASE_URL + URL_ROUTES[CHANGES],
    GROUPS: BASE_URL + URL_ROUTES[GROUPS]
}
