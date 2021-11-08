from tthk_scraper.models.group import Language, Group


def test_determine_language_by_code_russian():
    expected = Language.Russian
    assert expected == Group.determine_language_by_code('TARpv19')
    assert expected == Group.determine_language_by_code('VLOGpv21')
    assert expected == Group.determine_language_by_code('LOGITpv21')
    assert expected == Group.determine_language_by_code('VLOGgv20')


def test_determine_language_by_code_estonian():
    expected = Language.Estonian
    assert expected == Group.determine_language_by_code('MÜKgeMS21')
    assert expected == Group.determine_language_by_code('KRRgeÕ21')
    assert expected == Group.determine_language_by_code('MEHpe19')
    assert expected == Group.determine_language_by_code('ROOpe21')
