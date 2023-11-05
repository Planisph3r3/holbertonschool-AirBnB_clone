#!/usr/bin/python3
import unittest

from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_compare_attrs(self):
        review_attr = self.review.to_dict()
        self.assertIn("place_id", review_attr)
        self.assertIn("user_id", review_attr)
        self.assertIn("text", review_attr)
