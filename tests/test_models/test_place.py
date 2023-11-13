#!/bin/usr/python3
"""
    Testing Module for Place class.
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.place import Place
import unittest
import os

class TestPlace(unittest.TestCase):
    """test class for Place class."""
    def tearDown(self):
        # Code to run after each test method
        file_path = "file.json"

        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_create_place_with_required_arguments(self):
        """
        Place object can be created with required arguments.
        """
        place = Place(city_id="city_id", user_id="user_id", name="name")
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "name")

    def test_create_place_with_all_arguments(self):
        """
        Place object can be created with all arguments.
        """
        place = Place(
            city_id="city_id",
            user_id="user_id",
            name="name",
            description="description",
            number_rooms=5,
            number_bathrooms=3,
            max_guest=10,
            price_by_night=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenity_ids=["amenity1", "amenity2"]
        )
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
        place = Place(city_id="city_id", user_id="user_id", name="name")
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
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_invalid_arguments(self):
        """
        Place object can be created with invalid arguments.
        """     
        place = Place(city_id='123' , user_id='ABC', name=None)
        self.assertEqual(place.city_id , '123')
        self.assertEqual(place.user_id, 'ABC')
        self.assertEqual(place.name, None)

    def test_save_place_with_invalid_arguments(self):
        """
        Place object can be saved with invalid arguments.
        """
        place = Place(city_id="city_id", user_id="user_id", name="name")
        place.save()
        place.city_id = 123
        place.user_id = True
        place.name = None
        place.save()
        self.assertIsNotNone(place.updated_at)

if __name__ == "__main__":
    unittest.main()
