#!/bin/usr/python3
"""
    Testing Module for Review class.
    Author: Nour M. Ibrahim (nouribrahim1290@gmail.com)
"""

from models.review import Review
import unittest

class TestReview(unittest.TestCase):
    """Testing class for Review class."""

    def test_create_review_with_valid_arguments(self):
        """
            Review object can be created with valid place_id,
            user_id, and text arguments.
        """
        review = Review(place_id="123", user_id="456", text="Great place")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place")

    def test_save_review_successfully(self):
        """
            Review object can be saved successfully.
        """
        review = Review(place_id="123", user_id="456", text="Great place")
        review.save()
        self.assertIsNotNone(review.updated_at)

    def test_to_dict_method_returns_correct_dictionary_representation(self):
        """
            to_dict() method returns a dictionary
            representation of the Review object with correct
            keys and values
        """
        review = Review(place_id="123", user_id="456", text="Great place")
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "Great place")

    def test_create_review_without_required_arguments(self):
        """
            Review object cannot be created without required
            arguments (place_id, user_id, text)
        """
        with self.assertRaises(TypeError):
            review = Review()

    def test_place_id_argument_cannot_be_empty_string(self):
        """
            place_id argument cannot be an empty string
        """
        with self.assertRaises(ValueError):
            review = Review(place_id="", user_id="456", text="Great place")

    def test_user_id_argument_cannot_be_empty_string(self):
        """
            user_id argument cannot be an empty string.
        """
        with self.assertRaises(ValueError):
            review = Review(place_id="123", user_id="", text="Great place")