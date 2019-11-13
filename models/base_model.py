#!/usr/bin/python3

import models
import json
import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key is '__class__':
                    continue
                if key is 'created_at' or key is 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        idd = self.id
        diction = self.__dict__
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, idd, diction)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
