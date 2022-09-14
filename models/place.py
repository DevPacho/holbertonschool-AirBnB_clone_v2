#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from os import getenv as env
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review

"""association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))"""


class Place(BaseModel, Base if (env("HBNB_TYPE_STORAGE") == "db") else object):
    """Class that defines a Place"""

    if env("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        place_amenity = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     primary_key=True),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True))
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
        """amenities = relationship(
            "Amenity", secondary='place_amenity',
            back_populates='place_amenities', viewonly=False)"""

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns a list of 'Reviews' instances"""

            new_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    new_list.append(review)
            return new_list

        @property
        def amenities(self):
            """Returns a list of 'Amenities' instances"""

            new_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    new_list.append(amenity)
            return new_list

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities that handles append
            method for adding an Amenity.id
            """
            if (type(obj) == Amenity):
                self.amenity_ids.append(obj.id)
