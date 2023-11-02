#!/usr/bin/python3
import unittest
from time import sleep
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorage(unittest.TestCase):
    def test_file_path(self):
        self.assertIsNone(FileStorage.__file_path)

    def test_update_now(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        sleep(1)
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_save(self):
        model = BaseModel()
        self.assertIsNone(model.save())


if __name__ == '__main__':
    unittest.main()
