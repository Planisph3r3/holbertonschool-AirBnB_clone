#!/usr/bin/python3
import unittest
from models.user import user


class TestUser(unittest.TestCase):
    def setUp(self):
        self.Us = user()
        
    def test_compare_attrs(self):
        model_dict = self.Us.to_dict()
        self.assertIn("email", model_dict)
        self.assertIn("password", model_dict)
        self.assertIn("first_name", model_dict)
        self.assertIn("last_name", model_dict)










