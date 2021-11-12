from tthk_scraper.models.department import Department
from tthk_scraper.models.group.language import ESTONIAN_CODE_TRIGGER, Language, RUSSIAN_CODE_TRIGGER


class Group:
    def __init__(self,
                 code: str,
                 _language: Language = None,
                 department: Department = None):
        self.code = code
        self.language = _language
        self.department = department

    def determine_language(self):
        self.language = self.determine_language_by_code(self.code)

    @staticmethod
    def determine_language_by_code(code) -> Language:
        is_estonian = Group.get_language_trigger_position(code, ESTONIAN_CODE_TRIGGER)
        is_russian = Group.get_language_trigger_position(code, RUSSIAN_CODE_TRIGGER)
        return Language.Russian if is_russian > is_estonian else Language.Estonian

    @staticmethod
    def get_language_trigger_position(code, trigger) -> int:
        START_POSITION = 0
        END_POSITION = 7
        return code.find(trigger, START_POSITION, END_POSITION)
