import unittest
from io import StringIO
from unittest.mock import patch
from phonebook import *


class TestPhonebook(unittest.TestCase):

    def test_add(self):
        with patch('builtins.input', side_effect=['Oleg', 'Petrov', 'Oleg Petrov', '4546466', 'Kyiv']) as inp:
            with patch('phonebook.add') as rd:
                add()
                rd.call_args_list

    def test_search_name(self):
        with patch('builtins.input', return_value=['Ann']) as inp:
            with patch('phonebook.search_name') as rd:
                search_name()
                rd.call_args_list

    def test_search_lastname(self):
        with patch('builtins.input', return_value=['Ignatov']) as inp:
            with patch('phonebook.search_lastname') as rd:
                search_lastname()
                rd.call_args_list

    def test_phone(self):
        with patch('builtins.input', return_value=['0633288000']) as inp:
            with patch('phonebook.phone') as rd:
                phone()
                rd.call_args_list

    def test_dict_in_phonebook(self):
        self.assertIn({'name': 'Ann', 'surname': 'Ivanova', 'full_name': 'Ann Ivanova',
                       'phone': '0964448000', 'city': 'Kyiv'}, phonebook)

    def test_print(self):
        self.fake = StringIO()
        self.fake_out = patch('sys.stdout', new=self.fake)
        with self.fake_out:
            print_phonebook()
            self.assertIn('Ann', self.fake.getvalue())
            self.assertIn('Dmytro Ignatov', self.fake.getvalue())
            self.assertIn('0633288000', self.fake.getvalue())


if __name__ == '__main__':
    unittest.main()
