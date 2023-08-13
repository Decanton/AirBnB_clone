#!/usr/bin/python3
"""This module defines test for the User class"""


from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """This is the TestUser class"""
    def test_create(self):
        """Unittest for safe creation of an User"""
        User()
