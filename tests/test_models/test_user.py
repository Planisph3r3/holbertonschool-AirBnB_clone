#!/usr/bin/python3
import unittest
from models.user import user


class TestUser(unittest.TestCase):
    def setUp(self):
        self.Us = user()
        
    def test_compare_attrs(self):
        user_dict = self.Us.to_dict()
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)










