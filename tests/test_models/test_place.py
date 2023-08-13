#!/usr/bin/python3
"""This module defines test for the Place class"""


from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """This is the TestPlace class"""
    def test_create(self):
        """Unittest for safe creation of an Place"""
        Place()
