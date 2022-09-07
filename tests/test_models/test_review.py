#!/usr/bin/python3
""" This module test the 'Review' class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Testing the 'Review' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Testing type of attr place id """
        new = self.value(place_id="RandomIDPlacee23334-3dwq3")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Testing type of attr user id """
        new = self.value(user_id="Jssc-17")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Testing type of attr text """
        new = self.value(text="Qué dice Robert?")
        self.assertEqual(type(new.text), str)
