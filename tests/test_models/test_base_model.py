#!/usr/bin/python3
"""This module defines a Unittest for BaseModel Class"""


from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase
from uuid import UUID


class TestBaseModel(TestCase):
    """This is the TestBaseModel class"""
    def test_init(self):
        """Unittest for init"""
        obj = BaseModel()
        self.assertTrue(getattr(obj, 'id', None))
        self.assertTrue(getattr(obj, 'created_at', None))
        self.assertTrue(getattr(obj, 'updated_at', None))
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))
        self.assertTrue(isinstance(obj.id, str))
        UUID(obj.id)

    def test_to_dict(self):
        """Unitttest for BaseModel.to_dict"""

    def test_save(self):
        """Updates the public instance attribute updated_at to now"""

    def test_repr(self):
        """
        Unittest for str(BaseModel) and repr(BaseModel)
        """
