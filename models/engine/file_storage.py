#!usr/bin/python3

import json
import models
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp, f)

    def reload(self):
        #re_dict = {}
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                self.__objects = json.load(f)
                for key, value in self.__object.items():
                    self.new(self.__objects[value['__class__']](**value))
        except:
            pass
