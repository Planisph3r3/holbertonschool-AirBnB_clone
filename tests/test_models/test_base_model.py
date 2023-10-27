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

    def test_return(self):
        """
        Compara el retorno como None de save().
        """
        self.assertIsNone(self.bm.save())

    def test_to_dict(self):
        """
        Verificca sí el método to_dict(), regesa una instancia
        de diccionario.
        """
        self.assertIsInstance(self.bm.to_dict(), dict)

    def test_compare_attrs(self):
        """
        Verifica que contengan todos los atributos.
        """
        model_dict = self.bm.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)


if __name__ == "__main__":
    unittest.main()
