#!/usr/bin/python3
""" This module test the 'Place' class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Testing the 'Place' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Testing type of attr city id """
        new = self.value(city_id="AD500")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Testing type of attr user id """
        new = self.value(user_id="70922september")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Testing type of attr name """
        new = self.value(name="Andorra La Vella")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Testing type of attr description """
        new = self.value(description="My favorite country")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Testing type of attr number of rooms """
        new = self.value(number_rooms=17)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Testing type of attr number of bathrooms """
        new = self.value(number_bathrooms=18)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Testing type of attr max number of guests """
        new = self.value(max_guest=31)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Testing type of attr price by night """
        new = self.value(price_by_night=1718)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Testing type of attr latitude """
        new = self.value(latitude=37.774)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Testing type of attr longitude """
        new = self.value(longitude=-122.431)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ Testing type of attr amenity ids """
        new = self.value(amenity_ids=["Ps5", "Internet", "Games"])
        self.assertEqual(type(new.amenity_ids), list)
