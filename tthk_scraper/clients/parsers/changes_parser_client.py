from datetime import datetime
from typing import Optional, List

from bs4.element import ResultSet

from tthk_scraper.clients.parsers.base_parser_client import BaseParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.blueprints import ChangeCell


class ChangesParserClient(BaseParserClient):
    def parse(self, document) -> List[Change]:
        tables = self.parse_tables(document)
        processed_tables = [row for table in list(self.process_changes_tables(tables)) for row in table]
        changes = list(filter(lambda row: row is not None, processed_tables))
        return changes

    def process_changes_tables(self, tables: ResultSet) -> List[List[Change]]:
        for table in tables:
            processed_rows = self.process_changes_rows(table)
            yield list(processed_rows)

    def process_changes_rows(self, table: ResultSet) -> List[Change]:
        for row in self.parse_table_rows(table):
            if row is not None:
                yield self.process_changes_cells(row)

    def process_changes_cells(self, row: ResultSet) -> Optional[Change]:
        cells = self.parse_table_cells(row)
        if not self.validate(cells):
            return None
        date = datetime.strptime(cells[ChangeCell.Date.value].text, '%d.%m.%Y')
        group = cells[ChangeCell.Group.value].text
        lessons = cells[ChangeCell.Lessons.value].text
        teacher = cells[ChangeCell.Teacher.value].text
        change = Change(date=date,
                        group=group,
                        lessons=lessons,
                        teacher=teacher)
        status_trigger_cell = cells[ChangeCell.Room.value].text
        change.assign_status(status_trigger_cell)
        return change

    @staticmethod
    def validate(cells):
        return len(cells) != 0 and cells[ChangeCell.Date.value].text != "Kuupäev"
