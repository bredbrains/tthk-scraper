from enum import Enum

CHANGES = "changes"
GROUPS = "groups"
CONSULTATIONS = "consultations"


class ChangeCell(Enum):
    Date = 1
    Group = 2
    Lessons = 3
    Teacher = 4
    Room = 5
    Status = 6
