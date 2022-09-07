#!/usr/bin/python3
""" This module test the 'City' class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Testing the 'City' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Testing type of attr state id """
        new = self.value(state_id="JJSIdde888e-aadfmj")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Testing type of attr name """
        new = self.value(name="Anchorage")
        self.assertEqual(type(new.name), str)
