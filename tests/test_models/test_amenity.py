#!/usr/bin/python3
"""This module define test for the Amenity class"""


from models.amenity import Amenity
from unittest import TestCase


class TestAmenity(TestCase):
    """This is the TestAmenity class"""
    def test_create(self):
        """Unittest for safe creation of an Amenity"""
        Amenity()
