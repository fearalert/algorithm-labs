import unittest
import networkx as nx
import matplotlib.pyplot as plt
from main import *

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.url = "D:\\algorithms-lab\\graph\\test.edges"
        self.G = import_graph(self.url)

    def test_import_graph(self):
        self.assertIsInstance(self.G, nx.Graph)
        self.assertEqual(len(self.G.nodes()), 7)
        self.assertEqual(len(self.G.edges()), 7)

    def test_draw_graph(self):
        draw_graph(self.G)
        plt.close() 

    def test_get_average_deg(self):
        avg_degree = get_average_deg(self.G)
        self.assertAlmostEqual(avg_degree, 2.0)

    def test_get_density(self):
        E = 10
        N = 5
        density = get_density(E, N)
        self.assertAlmostEqual(density, 1.0)

    def test_get_clustering_coeff(self):
        clustering_coeff = get_clustering_coeff(self.G)
        self.assertAlmostEqual(clustering_coeff, 0.0)

    def test_get_diameter(self):
        # Manually verify the diameter by inspecting the graph
        self.assertEqual(get_diameter(self.G), None)

    def test_get_degree_distribution(self):
        # Run the function and visually verify the degree distribution plot
        get_degree_distribution(self.G)
        plt.close()  # Close the figure to prevent it from blocking subsequent tests

if __name__ == "__main__":
    unittest.main()
