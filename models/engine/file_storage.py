#!usr/bin/python3
"""
class FileStorage - this class serializate and deserializate JSON and instances
"""
import json
import os
from models.base_model import BaseModel
from models.User import User

dictionary = {'BaseModel': BaseModel, 'User': User}


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns a dictionary of __objects """
        return self.__objects

    def new(self, obj):
        """ sets the obj with key <obj class id> """
        id_obj = obj.__class__.__name__ + "." + obj.id
        self.__objects[id_obj] = obj

    def save(self):
        """ serializate __objects in the JSON file """
        dictt = {}
        for key, value in self.__objects.items():
            if not value:
                pass
            else:
                dictt[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(dictt, f)

    def reload(self):
        """ deserializate the JSON file in __objects """
        is os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dictionary[value['__class__']](**value))
