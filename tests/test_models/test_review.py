#!/usr/bin/python3
"""This module defines test for the Review class"""


from models.review import Review
from unittest import TestCase


class TestReview(TestCase):
    """This is the TestReview class"""
    def test_create(self):
        """Unittest for safe creation of an Review"""
        Review()
