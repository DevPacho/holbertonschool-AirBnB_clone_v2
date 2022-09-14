#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv as env


class City(BaseModel, Base if (env("HBNB_TYPE_STORAGE") == "db") else object):
    """ The city class, contains state ID and name """

    if env("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")

    else:
        name = ""
        state_id = ""
