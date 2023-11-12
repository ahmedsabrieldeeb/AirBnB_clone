#!/bin/usr/python3
"""Testing Module for Amenity class."""

import unittest
from datetime import datetime, timedelta


from models.base_model import BaseModel
from models.base_model import Amenity


class TestAmenity(unittest.TestCase):
    """Test Model for Amenity class."""

    def test_set_name_attribute(self):
        """
        Creating an instance of Amenity with a name attribute
        sets the name correctly.
        """
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

    def test_save_updates_updated_at(self):
        """
        Calling save() on an instance of Amenity updates
        the updated_at attribute.
        """
        amenity = Amenity(name="Gym")
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)

    def test_to_dict_returns_all_attributes(self):
        """Calling to_dict() on an instance of Amenity returns
        a dictionary with all attributes and their values,
        including the class name, created_at, and updated_at.
        """
        amenity = Amenity(name="Spa")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(
                amenity_dict["created_at"],
                amenity.created_at.isoformat()
                )
        self.assertEqual(
                amenity_dict["updated_at"],
                amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], "Spa")

    def test_no_arguments_sets_attributes_correctly(self):
        """
        Creating an instance of Amenity with no arguments sets the id,
        created_at, and updated_at attributes correctly.
        """
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_multiple_instances_with_same_name_return_different_objects(self):
        """
        Creating multiple instances of Amenity with the same name
        attribute returns different objects with different ids.
        """
        amenity1 = Amenity(name="Restaurant")
        amenity2 = Amenity(name="Restaurant")
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_update_name_attribute_and_save(self):
        """
        Updating the name attribute of an instance of Amenity
        and then calling save() updates the updated_at attribute
        and changes the name attribute.
        """
        amenity = Amenity(name="Bar")
        old_updated_at = amenity.updated_at
        amenity.name = "Pub"
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)
        self.assertEqual(amenity.name, "Pub")

    def test_non_string_name_attribute_raises_type_error(self):
        """
        Creating an instance of Amenity with a name attribute
        that is not a string raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Amenity(name=123)

    def test_no_arguments_sets_created_at_and_updated_at_to_current_time(self):
        """
        Creating an instance of Amenity with no arguments sets the
        created_at and updated_at attributes to the current time.
        """
        amenity = Amenity()
        now = datetime.now()
        self.assertAlmostEqual(
                amenity.created_at,
                now,
                delta=timedelta(seconds=1)
                )
        self.assertAlmostEqual(
                amenity.updated_at,
                now,
                delta=timedelta(seconds=1)
                )

    def test_set_id_attribute(self):
        """
        Creating an instance of Amenity with an id attribute sets
        the id attribute correctly.
        """
        amenity = Amenity(id="123")
        self.assertEqual(amenity.id, "123")

    def test_to_dict_returns_all_attributes_even_if_some_are_none(self):
        """
        Calling to_dict() on an instance of Amenity returns a dictionary
        with all attributes and their values, including the class name,
        created_at, and updated_at, even if some attributes are None.
        """
        amenity = Amenity(name="Parking")
        amenity.name = None
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(
                amenity_dict["created_at"],
                amenity.created_at.isoformat()
                )
        self.assertEqual(
                amenity_dict["updated_at"],
                amenity.updated_at.isoformat()
                )
        self.assertIsNone(amenity_dict["name"])

    def test_save_on_unsaved_instance_raises_attribute_error(self):
        """
        Calling save() on an instance of Amenity that has not been
        added to the storage raises a AttributeError.
        """
        amenity = Amenity(name="Conference Room")
        with self.assertRaises(AttributeError):
            amenity.save()

    def test_long_name_attribute_raises_value_error(self):
        """
        Creating an instance of Amenity with a name attribute that
        is longer than 128 characters raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Amenity(name="a" * 129)
