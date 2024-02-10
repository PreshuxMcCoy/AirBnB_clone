#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines common attributes/methods for
    other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(
                            self,
                            key,
                            datetime.strptime(
                                value,
                                '%Y-%m-%dT%H:%M:%S.%f'
                            ))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            storage.new(self)

    def __str__(self):
        """
        Returns string representation of BaseModel.
        """
        return ("[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id, self.__dict__
                                    ))

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime and calls the save() method of storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
