import unittest
from source.employee import Employee


class Employee_test(unittest.TestCase):
    def test_employee_details(self):
        test_employee = Employee("Abhishek", "Surya")
        self.assertEquals(test_employee.employee_first_name, "Abhishek")
        self.assertEquals(test_employee.employee_last_name, "Surya")
        self.assertEquals(
            test_employee.employee_email, "Abhishek.Surya@abhisheksurya.dev"
        )
        self.assertNotEquals(
            test_employee.employee_email, "AbhishekSurya@abhisheksurya.dev"
        )

    def test_employee_fullname(self):
        test_employee = Employee("Abhishek", "Surya")
        self.assertEqual(test_employee.get_fullname, "Surya, Abhishek")


if __name__ == "__main__":
    unittest.main()
