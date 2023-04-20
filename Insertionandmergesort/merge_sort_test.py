import unittest
from merge_sort import merge_sort

class mergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        A=[2,3,5,1,4,6]
        B=[1,2,3,4,5,6]
        C=[6,5,4,3,2,1]

        sortedList=[1,2,3,4,5,6]

        merge_sort(A,0,5)
        merge_sort(B,0,5)
        merge_sort(C,0,5)

        self.assertListEqual(A,sortedList)
        self.assertListEqual(B,sortedList)
        self.assertListEqual(C,sortedList)

if __name__  == "__main__":
    unittest.main()