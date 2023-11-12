#!/usr/bin/python3
"""
    Base Storage Module
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel():
    """Represent a BaseModel for Data Elements"""

    def __init__(self, *args, **kwargs):
        """
        Define a new Object instance of Base Model
        Args:
            id (string): The id of the object being created (Primary Key)
            created_at (datetime): The datetime Object at which
            the Object instance has been created.
            updated_at (datetime): The datetime Object at which
            the Object instance has been updated Last.
        """


        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(
                                self,
                                key,
                                datetime.strptime(
                                    val,
                                    '%Y-%m-%dT%H:%M:%S.%f')
                                )
                    else:
                        setattr(self, key, val)

    def __str__(self):
        """Return a string representation of the class"""

        return "[{:s}] ({:s}) {:s}".format(
                self.__class__.__name__,
                self.id,
                str(self.__dict__)
            )

    def save(self):
        "Save the latest created data and record update date"

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""

        rep = {
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }
        dict_copy = self.__dict__.copy()
        dict_copy.update(rep)
        return dict_copy
