#!/usr/bin/python3
"""Defines a class Review that is the template for review objects"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a review.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
