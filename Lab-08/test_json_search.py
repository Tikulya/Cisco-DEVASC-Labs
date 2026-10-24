
import unittest

from recursive_json_search import *
from test_data import *


class json_search_test(unittest.TestCase):

    def test_search_found(self):
        """proveryaet chto vse norm"""
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        """proveryaet chto net nepravil'nogo"""
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        """proveryaet chto spisok vozvrashaetsya"""
        self.assertIsInstance(json_search(key1, data), list)


if __name__ == '__main__':
    unittest.main()
# Fill the Python code in this file
