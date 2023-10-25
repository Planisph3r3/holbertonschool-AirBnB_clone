#!/usr/bin/python3
"""
Este módulo define la clase BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Esta clase define BaseModel
    """

    def __init__(self):
        """
        Este método inicializa lo sgte:
            id, created_at, updated_at
        Attr:
            id (str): Genera un id cada vez que se instancia.
            created_ad (str): Genera la hora y fecha cada vez
                    que se instancia un nuevo objeto.
            updated_at (str): Genera y actualiza la hora y fecha,
                    cada vez que se cambia nuestra instancia.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Este metodo regresa una representación de nuestra instancia

        Returns:
            str: Representación de instancia.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Este método actualiza la fecha de creación updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Este método regresa un diccionario.

        Returns:
            dict: Regresa un diccionario con los atributos de instancia.
        """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
