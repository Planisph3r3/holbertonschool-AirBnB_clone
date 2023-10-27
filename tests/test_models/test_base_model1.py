#!/usr/bin/python3
"""
Este modulo contiene los casos de prueba para
nuestra clase BaseModel.
"""


import unittest

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

    def test_isdict(self):
        """
        Compara el retorno como dict de to_dict().
        """
        self.assertIsInstance(self.bm.to_dict(), dict)

    def test_return(self):
        """
        Compara el retorno como None de save().
        """
        self.assertIsNone(self.bm.save())


if __name__ == "__main__":
    unittest.main()
