#!/usr/bin/python3
""" This module test the 'State' class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Testing the 'State' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Testing type of attr name """
        new = self.value(name="Alaska")
        self.assertEqual(type(new.name), str)
