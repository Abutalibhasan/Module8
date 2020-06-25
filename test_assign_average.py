import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_switch_average(self, A=None):
        x = assign_average.switch_average(A)
        self.assertEqual(x,A)
    def test_switch_average(self, B=None):
        x = assign_average.switch_average(B)
        self.assertEqual(x,B)
    def test_switch_average(self, C=None):
        x = assign_average.switch_average(C)
        self.assertEqual(x,C)
    def test_switch_average(self, D=None):
        x = assign_average.switch_average(D)
        self.assertEqual(x,D)
    def test_switch_average(self, E=None):
        x = assign_average.switch_average(E)
        self.assertEqual(x,E)

if __name__ == '__main__':
    unittest.main()
