import unittest


class Employee_test(unittest.TestCase):
    def test_email(self):
        emp1 = "test@test.com"
        self.assertEquals(emp1, "test@test.com")


if __name__ == "__main__":
    unittest.main()
