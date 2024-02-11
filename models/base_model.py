#!/usr/bin/python3
"""Defines the base class BaseModel"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Defines super class that handles objects"""
    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if hasattr(storage, 'new'):
                storage.new(self)

    def __str__(self):
        """Prints class name, id, and dictionary of class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' to the current time"""
        if hasattr(storage, 'save'):
            self.updated_at = datetime.now()
            storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/value pairs of an instance"""
        obj_dict = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = value.isoformat()

        return obj_dict

