import unittest
from random import random
from dynamic import knapsack_dynamic
from greedy import knapsack_greedy
from bruteforce import build_items, powerset, knapsack_brute_force01, knapsack_brute_force_fractional

class KnapsackTestCase(unittest.TestCase):
    def test_knapsack01(self):
        items = [(0, 5, 10), (1, 10, 30), (2, 3, 15)]
        max_weight = 10
        expected_result = ([(1, 10, 30)], 10, 30) 

        result_bruteforce = knapsack_brute_force01(items, max_weight)
        result_dynamic = knapsack_dynamic(items, max_weight)
        self.assertEqual(result_dynamic, expected_result)
        self.assertEqual(result_bruteforce, expected_result)

    def test_knapsack_fractional(self):
        items = [(0, 5, 10), (1, 10, 30), (2, 3, 15)]
        max_weight = 10
        expected_result = ([(2, 3, 15), (1, 7.0, 21.0)], 10, 36.0) 

        result_greedy = knapsack_greedy(items, max_weight)
        result_bruteforce = knapsack_brute_force_fractional(items, max_weight)
        self.assertEqual(result_greedy, expected_result)
        self.assertEqual(result_bruteforce, expected_result)

    def test_build_items(self):
        items = build_items(5)
        self.assertEqual(len(items), 5) 

    def test_powerset(self):
        # Test the powerset function
        items = [(0, 5, 4), (1, 4, 2)]
        result = powerset(items)
        expected_result = [[], [(0, 5, 4)], [(1, 4, 2)], [(0, 5, 4), (1, 4, 2)]]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
