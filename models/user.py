#!/usr/bin/python3
"""This module defines a User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
