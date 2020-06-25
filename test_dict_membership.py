import unittest
from more_fun_with_collections import dict_membership



class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        res = dict_membership.in_dict()
        self.assertNotEquals(res, True)
    def test_in_dict_false(self):
        res = dict_membership.in_dict()
        self.assertNotEquals(res, False)


if __name__ == '__main__':
    unittest.main()
