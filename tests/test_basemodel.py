import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.bm = BaseModel()
        
    def test_init(self):
        self.assertIsInstance(self.bm.id, str)
