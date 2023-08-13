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

    def test_unique(self):
        """Unittest for unique ids"""
        ob1 = BaseModel()
        ob2 = BaseModel()
        ob3 = BaseModel()
        self.assertNotEqual(ob1.id, ob2.id)
        self.assertNotEqual(ob2.id, ob3.id)
        self.assertNotEqual(ob3.id, ob1.id)

    def test_init_args(self):
        """Unittest for creation with different arguments"""
        ob1 = BaseModel('one')
        ob2 = BaseModel('arg', kw='two')
        ob3 = BaseModel(name='someone')
        self.assertTrue(getattr(ob1, 'id', None) is not None)
        self.assertTrue(getattr(ob2, 'id', None) is None)
        self.assertTrue(getattr(ob3, 'id', None) is None)

    def test_to_dict(self):
        """Unitttest for BaseModel.to_dict"""
        obj = BaseModel()
        objdict = obj.to_dict()
        self.assertTrue(isinstance(objdict, dict))
        self.assertEqual(objdict.get('__class__', None), 'BaseModel')

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
