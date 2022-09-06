#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="state")

    else:
        @property
        def cities(self):
            """Returns the list of City instances"""
            new_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
