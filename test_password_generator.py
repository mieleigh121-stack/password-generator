import unittest
from password_generator import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(10, True, False, False, False)
        self.assertEqual(len(password), 10)

    def test_only_digits(self):
        password = generate_password(8, False, False, True, False)
        self.assertTrue(password.isdigit())

    def test_no_character_types(self):
        password = generate_password(8, False, False, False, False)
        self.assertIsNone(password)

    def test_upper_and_lower(self):
        password = generate_password(12, True, True, False, False)
        self.assertEqual(len(password), 12)


if __name__ == "__main__":
    unittest.main()
    