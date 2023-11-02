#!/usr/bin/python3
import unittest
from time import sleep
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestStorage(unittest.TestCase):
    def test_file_path(self):
        self.assertIsNone(FileStorage.__file_path)

    def test_update_now(self):
        bs = BaseModel()
        sleep(1)
        bs.save()
        self.assertIsNot(bs.created_at, bs.updated_at)
