#!/usr/bin/python3
"""This module defines test for the City class"""


from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """This is the TestCity class"""
    def test_create(self):
        """Unittest for safe creation of an City"""
        City()
