#!/usr/bin/python3
"""Testing Module for BaseModel class"""

import unittest
import datetime
from uuid import uuid4

from models.base_model import BaseModel 
from models import storage


class TestBaseModel(unittest.TestCase):
    """Testing class for BaseModel."""

    def test_create_instance_with_no_arguments(self):
        """
        Creating a new instance of BaseModel with no
        arguments sets the id to a unique string, created_at
        and updated_at to the current datetime, and adds
        the instance to the storage.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(
                storage.all()[instance.__class__.__name__ + '.' + instance.id],
                instance
                )

    def test_create_instance_with_arguments(self):
        """
            Creating a new instance of BaseModel with
            arguments sets the corresponding attributes to
            the given values.
        """
        id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        instance = BaseModel(
                id=id,
                created_at=created_at,
                updated_at=updated_at
                )
        self.assertIsInstance(instance, BaseModel)
        self.assertEqual(instance.id, id)
        self.assertEqual(instance.created_at, created_at)
        self.assertEqual(instance.updated_at, updated_at)

    def test_save_method(self):
        """
        Calling save() on an instance of BaseModel updates
        the updated_at attribute to the current datetime and
        saves the instance to the storage."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertEqual(
                storage.all()[instance.__class__.__name__ + '.' + instance.id],
                instance
                )

    def test_to_dict_method(self):
        """
        Calling to_dict() on an instance of BaseModel returns
        a dictionary representation of the instance with the
        class name, created_at, and updated_at attributes.
        """
        instance = BaseModel()
        dict_rep = instance.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertEqual(dict_rep['__class__'], instance.__class__.__name__)
        self.assertEqual(
                dict_rep['created_at'],
                instance.created_at.isoformat()
                )
        self.assertEqual(
                dict_rep['updated_at'],
                instance.updated_at.isoformat()
                )

    def test_create_instance_with_id_argument(self):
        """Creating a new instance of BaseModel with an id
        argument sets the id to the given value."""
        id = str(uuid4())
        instance = BaseModel(id=id)
        self.assertEqual(instance.id, id)

    def test_create_instance_with_invalid_datetime_argument(self):
        """Creating a new instance of BaseModel with
        a created_at or updated_at argument in an invalid
        format raises a ValueError."""
        with self.assertRaises(ValueError):
            BaseModel(created_at='2022-01-01')
        with self.assertRaises(ValueError):
            BaseModel(updated_at='2022-01-01')

    def test_save_method_with_no_changes(self):
        """Calling save() on an instance of BaseModel with no
        changes does not update the updated_at attribute."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertEqual(instance.updated_at, old_updated_at)

    def test_to_dict_method_with_additional_attributes(self):
        """Calling to_dict() on an instance of BaseModel with
        additional attributes returns a dictionary
        representation of the instance with the additional attributes."""
        instance = BaseModel()
        instance.name = "Test"
        dict_rep = instance.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertEqual(
                dict_rep['__class__'],
                instance.__class__.__name__
                )
        self.assertEqual(
                dict_rep['created_at'],
                instance.created_at.isoformat()
                )
        self.assertEqual(
                dict_rep['updated_at'],
                instance.updated_at.isoformat()
                )
        self.assertEqual(dict_rep['name'], "Test")

    def test_create_subclass_instance(self):
        """Creating a new instance of a subclass of BaseModel
        sets the __class__ attribute to the subclass name."""
        class SubModel(BaseModel):
            pass
        instance = SubModel()
        self.assertEqual(instance.__class__.__name__, "SubModel")

    def test_create_instance_with_valid_datetime_argument(self):
        """Creating a new instance of BaseModel with
        a created_at or updated_at argument in a valid format
        sets the corresponding attributes to the given datetime."""
        created_at = datetime(2022, 1, 1)
        updated_at = datetime(2022, 1, 2)
        instance = BaseModel(created_at=created_at, updated_at=updated_at)
        self.assertEqual(instance.created_at, created_at)
        self.assertEqual(instance.updated_at, updated_at)

    def test_save_method_updates_storage(self):
        """Calling save() on an instance of BaseModel updates
        the instance in the storage."""
        instance = BaseModel()
        instance.save()
        self.assertEqual(
                storage.all()[instance.__class__.__name__ + '.' + instance.id],
                instance
                )

    def test_to_dict_method_with_no_attributes(self):
        """Calling to_dict() on an instance of BaseModel with
        no attributes returns a dictionary representation of
        the instance with only the class name, created_at,
        and updated_at attributes."""
        instance = BaseModel()
        dict_rep = instance.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertEqual(dict_rep['__class__'], instance.__class__.__name__)
        self.assertEqual(
                dict_rep['created_at'],
                instance.created_at.isoformat()
                )
        self.assertEqual(
                dict_rep['updated_at'],
                instance.updated_at.isoformat()
                )

if __name__ == "__main__":
    unittest.main()
