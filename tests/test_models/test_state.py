#!/usr/bin/python3
"""This module defines test for the State class"""


from models.state import State
from unittest import TestCase


class State(TestCase):
    """This is the State class"""
    def test_create(self):
        """Unittest for safe creation of an State"""
        State()
