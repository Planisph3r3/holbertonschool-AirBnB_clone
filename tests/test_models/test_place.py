#!/usr/bin/python3
import unittest

from models.place import Place


class TestCity(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_compare_attrs(self):
        place_attr = self.place.to_dict()
        self.assertIn("city_id", place_attr)
        self.assertIn("user_id", place_attr)
        self.assertIn("name", place_attr)
        self.assertIn("description", place_attr)
        self.assertIn("number_rooms", place_attr)
        self.assertIn("number_bathrooms", place_attr)
        self.assertIn("max_guest", place_attr)
        self.assertIn("price_by_night", place_attr)
        self.assertIn("latitude", place_attr)
        self.assertIn("longitude", place_attr)
        self.assertIn("amenity_ids", place_attr)
