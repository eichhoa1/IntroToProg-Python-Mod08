# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# Adam Eichholz, 9/3/2025, Created Script.
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("John", "Doe", "1900-01-01", 3)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "1900-01-01")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_rating(self):
        with self.assertRaises(ValueError):
            employee = Employee("John", "Doe", "1900-01-01", 1000)

    def test_employee_str(self):
        employee = Employee("John", "Doe", "1900-01-01", 3) #tests the __str__() magic method
        self.assertEqual(str(employee), "John,Doe,1900-01-01,3")


if __name__ == '__main__':
    unittest.main()