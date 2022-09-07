#!/usr/bin/python3
""" This module test the 'Amenity' class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Testing the 'Amenity' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Testing type of attr name """
        new = self.value(name="5GWifi")
        self.assertEqual(type(new.name), str)
