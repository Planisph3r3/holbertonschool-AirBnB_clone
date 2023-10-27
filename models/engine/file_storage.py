#!/usr/bin/python3
import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.__dict__

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                json.load(f)
        else:
            pass
