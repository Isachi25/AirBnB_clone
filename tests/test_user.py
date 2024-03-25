#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()
