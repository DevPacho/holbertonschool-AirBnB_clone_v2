#!/usr/bin/python3
""" Testing the console module """

import unittest
from models.engine import db_storage
from models.engine.db_storage import DBStorage


class TestConsole(unittest.TestCase):
    """ Testing the DBStorage class """

    def test_documentation(self):
        """ Testing module docstrings documentation"""

        self.assertTrue(db_storage.__doc__)
        self.assertTrue(db_storage.DBStorage.__doc__)

    def test_methods_doc(self):
        """ Testing all docstrings documentation of each DBStorage method"""

        for all_methods in dir(DBStorage):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()
