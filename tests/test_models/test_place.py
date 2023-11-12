#!/bin/usr/python3
"""
    Testing Module for Place class.
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.place import Place
import unittest

class TestPlace(unittest.TestCase):
    """test class for Place class."""

    def test_create_place_with_required_arguments(self):
        """
            Place object can be created with required arguments.
        """
        place = Place("city_id", "user_id", "name")
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "name")

    def test_create_place_with_all_arguments(self):
        """
            Place object can be created with all arguments.
        """
        place = Place("city_id", "user_id", "name", "description", 5, 3, 10, 100, 37.7749, -122.4194, ["amenity1", "amenity2"])
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "name")
        self.assertEqual(place.description, "description")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_save_place(self):
        """
            Place object can be saved successfully.
        """
        place = Place("city_id", "user_id", "name")
        place.save()
        self.assertIsNotNone(place.updated_at)

    def test_create_place_with_empty_arguments(self):
        """
            Place object can be created with empty arguments.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, "")
        self.assertEqual(place.number_bathrooms, "")
        self.assertEqual(place.max_guest, "")
        self.assertEqual(place.price_by_night, "")
        self.assertEqual(place.latitude, "")
        self.assertEqual(place.longitude, "")
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_invalid_arguments(self):
        """
            Place object can be created with invalid arguments.
        """
        place = Place(123, True, None)
        self.assertEqual(place.city_id, 123)
        self.assertEqual(place.user_id, True)
        self.assertEqual(place.name, None)

    def test_save_place_with_invalid_arguments(self):
        """
            Place object can be saved with invalid arguments.
        """
        place = Place("city_id", "user_id", "name")
        place.save()
        place.city_id = 123
        place.user_id = True
        place.name = None
        place.save()
        self.assertIsNotNone(place.updated_at)

if __name__ == "__main__":
    unittest.main()
