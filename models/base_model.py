#!/bin/env python3
"""The Basemodel class for my AirBnB"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage as storage  

class BaseModel:
    """A class that defines all common attributes of other classes"""
    id = "[BaseModel]"

    def __init__(self, *args, **kwargs):
        """Instantiation of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            storage.new(self, self)  # Call new(self) method on storage for new instances
            


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance"""
        self.updated_at = datetime.now()
        storage.save(self)  # Call save() method of storage

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

