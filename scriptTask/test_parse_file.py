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
        expected_statement = [
            'INSERT INTO users (name,surname,email) VALUES ("John","Smith","jsmith@gmail.com")',
            'INSERT INTO users (name,surname,email) VALUES ("Hamish","Jones","ham@seek.com")',
            'INSERT INTO users (name,surname,email) VALUES ("Phil","Carry","phil@open.edu.au")',
            'INSERT INTO users (name,surname,email) VALUES ("Johnny","O\'Hare","john@yahoo.com.au")',
            'INSERT INTO users (name,surname,email) VALUES ("Mike","O\'Connor","mo\'connor@cat.net.nz")',
            'INSERT INTO users (name,surname,email) VALUES ("William","Smythe","happy@ent.com.au")',
            'INSERT INTO users (name,surname,email) VALUES ("Hamish","Jones","ham@seek.com")',
            'INSERT INTO users (name,surname,email) VALUES ("Sam!!","Walters","sam!@walters.org")',
            'INSERT INTO users (name,surname,email) VALUES ("Daley","Thompson","daley@yahoo.co.nz")',
            'INSERT INTO users (name,surname,email) VALUES ("Kevin","Ruley","kevin.ruley@gmail.com")',
        ]
        self.assertEqual(statements,expected_statement)
