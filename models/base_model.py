#!/usr/bin/python3
"""
class base - this class defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
#from models import storage
import models
class BaseModel:
    """ Class Base Model """
    def __init__(self, *args, **kwargs):
        """ create a instance with an representation of dictionary """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], date_format)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ print [class name] (id) (__dict__) """
        idd = self.id
        diction = self.__dict__
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, idd, diction)

    def save(self):
        """ update with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of a instance """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
