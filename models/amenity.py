#!/bin/usr/python3
"""
    Amenity Identification Module
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an Amenity Object inheriting BaseModel

        ARGUMENTS:
        ----------
        name (string): amenity name
    """

    name = ""
