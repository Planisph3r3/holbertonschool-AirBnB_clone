#!/usr/bin/python3
"""
Este modulo contiene los casos de prueba para
nuestra clase BaseModel.
"""


import unittest
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Esta clase define los casos de prueba.
    """

    def setUp(self):
        """
        Se crea una instancia de nuestra clase BaseModel
        """
        self.bm = BaseModel()

    def test_init(self):
        """
        Se comparan los atributos con los tipos de datos.
        """
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
