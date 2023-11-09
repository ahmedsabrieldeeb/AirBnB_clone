#!/bin/usr/python3
"""
    Place Identification Model
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        Represent a Place Object inheriting BaseModel

        ARGUMENTS:
        ----------
        city_id (string): id of the city where the place lies,
                            it will be City.id
        user_id (string): id of the user choosing the city,
                            it will be User.id
        name (string): name of the place
        description (string): specifications to describe the place.
        number_rooms (int): number of rooms in place.
        number_bathrooms (int): number of bathrooms in place.
        max_guest: maximum number of guests allowed in the place.
        price_by_night (int): cost of booking the place per night.
        latitude (float): latitude of place location.
        longitude (float): lognitude of place location.
        amenity_ids (List(string)): a list of amenity ids for this place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = []

