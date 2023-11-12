#!/bin/usr/python3
"""
    Testing Module for City class.
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.city import City
import unittest
import os

class TestCity(unittest.TestCase):
    """Testing class for City Module."""
    def tearDown(self):
        # Code to run after each test method
        file_path = "file.json"

        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_create_city_with_state_id_and_name(self):
        """
            City object can be created with state_id and name.
        """
        city = City(state_id="123", name="New York")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    def test_save_and_update_city(self):
        """
            City object can be saved and updated.
        """
        city = City(state_id="123", name="New York")
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, initial_updated_at)

    def test_convert_city_to_dict(self):
        """
            City object can be converted to a dictionary.
        """
        city = City(state_id="123", name="New York")
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "123")
        self.assertEqual(city_dict["name"], "New York")

    def test_create_city_without_state_id_and_name(self):
        """
            City object can be created without state_id and name.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_create_city_with_invalid_state_id_and_name(self):
        """
            City object can be created with invalid state_id and name.
        """
        city = City(state_id=123, name=456)
        self.assertEqual(city.state_id, 123)
        self.assertEqual(city.name, 456)

    def test_save_city_without_changes(self):
        """
            City object can be saved without changes.
        """
        city = City(state_id="123", name="New York")
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, initial_updated_at)

if __name__ == "__main__":
    unittest.main()
