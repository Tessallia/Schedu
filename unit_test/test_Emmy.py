from unittest import TestCase

from file_handling.SQL.sql_handler import SQL_handler

class TestSQL_handler(TestCase):

    def setUp(self) -> None:
        handler = SQL_handler(True)

    def test_logical_statemnt(self):
        pass

    def test_connect(self):
        self.fail()

    def test_create_database(self):
        self.fail()

    def test_reset_database(self):
        self.fail()

    def test_get_table_info(self):
        self.fail()

    def test_get_cols(self):
        self.fail()

    def test_execute_statement(self):
        self.fail()
