from tthk_scraper.models.group import Language, Group


def test_determine_language_by_code_russian():
    assert Language.Russian == Group.determine_language_by_code('TARpv19')
    assert Language.Russian == Group.determine_language_by_code('VLOGpv21')
    assert Language.Russian == Group.determine_language_by_code('LOGITpv21')
    assert Language.Russian == Group.determine_language_by_code('VLOGgv20')


def test_determine_language_by_code_estonian():
    assert Language.Estonian == Group.determine_language_by_code('MÜKgeMS21')
    assert Language.Estonian == Group.determine_language_by_code('KRRgeÕ21')
    assert Language.Estonian == Group.determine_language_by_code('MEHpe19')
    assert Language.Estonian == Group.determine_language_by_code('ROOpe21')
