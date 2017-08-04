from unittest import TestCase
from user_upload import parse_file, construct_statements


class UT_file(TestCase):
    def test_parse_file(self):
        header, values = parse_file("./users.csv")
        self.assertEqual(header, ['name', 'surname', 'email\t'])
        self.assertIsNotNone(values)

    def test_construct_statements(self):
        header, values = parse_file("./users.csv")
        statements = construct_statements(header, values)
        self.assertIsNotNone(statements)
