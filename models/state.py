#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv as env


class State(BaseModel, Base if (env("HBNB_TYPE_STORAGE") == "db") else object):
    """ State class """

    if env("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of City instances"""
            new_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
