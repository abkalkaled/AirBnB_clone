#!/use/bin/python3
"""This creates user"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class for user object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
