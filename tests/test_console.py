#!/usr/bin/python3
""" Testing the console module """

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Testing the HBNBCommand class of the Console """

    def test_documentation(self):
        """ Testing module docstrings documentation"""

        self.assertTrue(console.__doc__)
        self.assertTrue(console.HBNBCommand.__doc__)

    def test_methods_doc(self):
        """ Testing all docstrings documentation of each console method"""

        for all_methods in dir(HBNBCommand):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()
