#!/bin/usr/python3
"""
    Testing Module for State class.
    Author: Nour M. Ibrahim (nouribrahim1290#gmail.com)
"""

from models.state import State
import unittest

class TestState(unittest.TestCase):
    """Testing State class."""

    def test_create_state_with_name_attribute(self):
        """
            State object can be created with a name attribute.
        """
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_save_and_update_state(self):
        """
            State object can be saved and updated.
        """
        state = State(name="California")
        state.save()
        self.assertIsNotNone(state.updated_at)

    def test_convert_to_dict(self):
        """
            State object can be converted to a dictionary representation.
        """
        state = State(name="California")
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["created_at"], state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], state.updated_at.isoformat())

    def test_create_state_with_non_string_name_attribute(self):
        """
            State object can be created with non-string name attribute.
        """
        state = State(name=123)
        self.assertEqual(state.name, 123)

    def test_create_state_with_empty_name_attribute(self):
        """
            State object can be created with empty name attribute.
        """
        state = State(name="")
        self.assertEqual(state.name, "")

    def test_create_state_with_no_name_attribute(self):
        """
            State object can be created with no name attribute.
        """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
