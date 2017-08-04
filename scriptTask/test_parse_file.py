from unittest import TestCase
from user_upload import parse_file

class TestParse_file(TestCase):

    def test_parse_file(self):
        header, values = parse_file("./users.csv")
        self.assertEqual(header,['name','surname','email\t'])
        self.assertIsNotNone(values)