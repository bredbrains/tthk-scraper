from abc import abstractmethod

from bs4 import BeautifulSoup
from bs4.element import ResultSet

TABLE_SELECTOR = 'table'
TABLE_ROW_SELECTOR = 'tr'
TABLE_CELL_SELECTOR = 'td'


class BaseParserClient:
    @abstractmethod
    def parse(self, document):
        pass

    @staticmethod
    def parse_tables(document: BeautifulSoup) -> ResultSet:
        return document.findChildren(TABLE_SELECTOR)

    @staticmethod
    def parse_table_rows(table: ResultSet) -> ResultSet:
        return table.find_all(TABLE_ROW_SELECTOR)

    @staticmethod
    def parse_table_cells(row: ResultSet) -> ResultSet:
        return row.find_all(TABLE_CELL_SELECTOR)
