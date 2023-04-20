import unittest
from linear_search import linear_search

class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values=[8,6,8,7,2,9,5,1,5,4]
        values1=range(10000)
        self.assertEqual(linear_search(values,8),0)
        self.assertEqual(linear_search(values,3),-1)
        self.assertEqual(linear_search(values,9),5)
        self.assertEqual(linear_search(values,4),9)
        self.assertEqual(linear_search(values1,1000),1000)
        self.assertEqual(linear_search(values1,2000),2000)
        self.assertEqual(linear_search(values1,9999),9999)


if __name__ == '__main__':
    unittest.main()