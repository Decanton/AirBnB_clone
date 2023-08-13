#!/usr/bin/python3
"""This module defines a Unittest for BaseModel Class"""


from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase
from uuid import UUID

import re


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
        obj = BaseModel()
        self.assertTrue(isinstance(obj.to_dict(), dict))

    def test_save(self):
        """Tests that updated_at is updated to now"""
        obj = BaseModel()
        then = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, then)

    def test_repr(self):
        """
        Unittest for str(BaseModel) and repr(BaseModel)
        """
        obj = BaseModel()
        pattern = f'^\\[BaseModel\\] \\({obj.id}\\) \\{{.*\\}}$'
        self.assertTrue(re.search(pattern, str(obj)))
