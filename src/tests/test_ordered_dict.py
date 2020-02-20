import unittest
from omnitrade_api.ordered_dict import ordered_dict

class TestOrderedDictMethods(unittest.TestCase):

    def test_ordered_dict(self):
        dictionary = { 'a': 1, 'b': 2, 'c': 3}
        
        self.assertEqual(ordered_dict(dictionary), [('a', 1),('b', 2),('c', 3)])

