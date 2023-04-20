import unittest
from insertion_sort import insertion_sort

class insertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        A=[2,3,5,1,4,6]
        B=[1,2,3,4,5,6]
        C=[6,5,4,3,2,1]

        sortedList=[1,2,3,4,5,6]

        insertion_sort(A)
        insertion_sort(B)
        insertion_sort(C)

        self.assertListEqual(A,sortedList)
        self.assertListEqual(B,sortedList)
        self.assertListEqual(C,sortedList)

if __name__  == "__main__":
    unittest.main()