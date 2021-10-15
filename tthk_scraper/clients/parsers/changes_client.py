from datetime import datetime
from typing import Optional, List

from bs4 import ResultSet

from tthk_scraper.clients.parsers.base_parser_client import BaseParserClient
from tthk_scraper.models.change import Change
from tthk_scraper.utils.blueprints import CHANGES, ChangeCell
from tthk_scraper.utils.urls import URLS


class ChangesParserClient(BaseParserClient):
    def __init__(self):
        url = URLS.get(CHANGES)
        super().__init__(url)

    def parse(self) -> List[Change]:
        document = self.open_page()
        tables = self.parse_tables(document)
        processed_tables = [row for table in list(self.process_changes_tables(tables)) for row in table]
        changes = list(filter(lambda row: row is not None, processed_tables))
        return changes

    def parse_by_date(self, received_date: str) -> List[Change]:
        changes = self.parse()
        date = datetime.strptime(received_date, '%Y-%m-%d')
        for change in changes:
            print(f"Received date: {date.strftime('%Y-%m-%d')}, change date: {change.date.strftime('%Y-%m-%d')}")
        changes = list(filter(lambda change: change.date.strftime('%Y-%m-%d') == date.strftime('%Y-%m-%d'), changes))
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
        if not ChangesParserClient._validate_change_row(cells):
            return None
        date = datetime.strptime(cells[ChangeCell.Date.value].text, '%d.%m.%Y')
        group = cells[ChangeCell.Group.value].text
        lessons = cells[ChangeCell.Lessons.value].text
        teacher = cells[ChangeCell.Teacher.value].text
        change = Change(date=date, group=group,
                        lessons=lessons, teacher=teacher)
        status_trigger_cell = cells[ChangeCell.Room.value].text
        change.assign_status(status_trigger_cell)
        return change

    @staticmethod
    def _validate_change_row(cells):
        return len(cells) != 0 and cells[ChangeCell.Date.value].text != "Kuupäev"
