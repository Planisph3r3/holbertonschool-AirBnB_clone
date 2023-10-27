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

    def test_compare_attrs(self):
        """
        Verifica que contengan todos los atributos.
        """
        model_dict = self.bm.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_methods_magic_str(self):
        """
        Compara la salida del método magic __str__.
        """
        bm = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_output)


if __name__ == "__main__":
    unittest.main()
