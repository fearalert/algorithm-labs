import unittest
from binary_search import binary_search

class SearchTestCase(unittest.TestCase):
    def test_binary_search(self):
        values=[0,1,3,5,7,2,1,6]
        values1=range(10000)
        self.assertEqual(binary_search(values,1),1)
        self.assertEqual(binary_search(values,3),2)
        self.assertEqual(binary_search(values,5),3)
        self.assertEqual(binary_search(values,8),-1)
        self.assertEqual(binary_search(values1,1000),1000)
        self.assertEqual(binary_search(values1,2000),2000)
        self.assertEqual(binary_search(values1,9999),9999)


if __name__ == '__main__':
    unittest.main()