#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv as e


class Amenity(BaseModel, Base if (e("HBNB_TYPE_STORAGE") == "db") else object):
    """Class that defines a Amenity"""

    if e("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship('Place', secondary='place_amenity')
    else:
        name = ""
