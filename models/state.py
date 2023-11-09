#!/bin/usr/python3
"""
    State Identification Module
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent State Object interting BaseModel

        ARGUMENTS:
        ---------
        name (string): state name
    """

    name = ""
