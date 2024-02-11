#!/usr/bin/python3
"""Defines a class Amenity for handling amenities"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that handles amenities throughout the site.

    Attribute:
    name (str) of amenity
    """
    name = ""
