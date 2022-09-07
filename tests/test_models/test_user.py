#!/usr/bin/python3
""" This module test the 'User' class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Testing the 'User' class """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Testing type of attr name """
        new = self.value(first_name="Robert")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Testing type of attr last name """
        new = self.value(last_name="Ramírez")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Testing type of attr email """
        new = self.value(email="holbies@holbertonstudents.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing type of attr password """
        new = self.value(password="parchese123")
        self.assertEqual(type(new.password), str)
