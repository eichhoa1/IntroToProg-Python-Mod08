# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# Adam Eichholz, 9/3/2025, Created Script.
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch

from data_classes import Employee
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data= []
        self.employee_type = Employee

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for student data
        with patch('builtins.input', side_effect=['John', 'Doe', '1900-01-01',3]):
            IO.input_employee_data(self.employee_data, self.employee_type)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Doe')
            self.assertEqual(self.employee_data[0].review_date, '1900-01-01')
            self.assertEqual(self.employee_data[0].review_rating, 3)

if __name__  == "__main__":
    unittest.main()