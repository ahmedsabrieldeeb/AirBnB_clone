#!/bin/usr/pthon3
"""
    Testing Module for User class.
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.user import User
import unittest
import os

class TestUser(unittest.TestCase):
    """Testing User class."""
    def tearDown(self):
        # Code to run after each test method
        file_path = "file.json"

        # Check if the file exists before attempting to delete
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_valid_user_creation(self):
        """
            Creating a new User object with valid email, password,
            first_name, and last_name should set the corresponding
            attributes correctly.
        """
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_save(self):
        """
            Calling save() on a User object should update the updated_at
            attribute and save the object to storage.
        """
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)

    def test_user_to_dict(self):
        """
            Calling to_dict() on a User object should return a dictionary
            representation of the object with the correct keys and values.
        """
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    # def test_invalid_user_creation(self):
    #     """
    #         Creating a new User object with invalid email, password,
    #         first_name, or last_name should raise a ValueError.
    #     """
    #     with self.assertRaises(ValueError):
    #         user = User(email="invalid_email", password="password", first_name="John", last_name="Doe")
    #     with self.assertRaises(ValueError):
    #         user = User(email="test@example.com", password="", first_name="John", last_name="Doe")
    #     with self.assertRaises(ValueError):
    #         user = User(email="test@example.com", password="password", first_name="", last_name="Doe")
    #     with self.assertRaises(ValueError):
    #         user = User(email="test@example.com", password="password", first_name="John", last_name="")

    def test_empty_user_creation(self):
        """
            Creating a new User object with no arguments should set the id,
            created_at, and updated_at attributes correctly.
        """
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # def test_unsaved_user_save(self):
    #     """
    #         Calling save() on a User object that has not been added to
    #         storage should raise a ValueError.
    #     """
    #     user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
    #     with self.assertRaises(ValueError):
    #         user.save()

if __name__ == "__main__":
    unittest.main()
