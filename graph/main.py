import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import collections

# header_list = ["a", "b", "w"]
header_list = ["a", "b", "w", "y"]
E = pd.read_csv('D:\\algorithms-lab\\graph\\aves-songbird-social.edges', sep=" ", header=None, names=header_list)

G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
nx.draw(G)

# Add numbers to the nodes
node_labels = {node: str(node) for node in G.nodes()}

# Draw the network with node labels
nx.draw(G, with_labels=True, labels=node_labels)

degrees = G.degree()

avg_degree = sum(dict(degrees).values()) / G.number_of_nodes()

density = (2 * G.number_of_edges()) / (G.number_of_nodes() * (G.number_of_nodes() - 1))

def get_clustering_coeff(G):
    clusters = []
    for node in G.nodes():
        neighbors = [neighbor for neighbor in G.neighbors(node)]
        ki = len(neighbors)
        subgraph = G.subgraph(neighbors)
        ei = subgraph.number_of_edges()

        if ki != 0 and ki != 1:
            ci = (2 * ei) / (ki * (ki - 1))
        else:
            ci = 0
        clusters.append(ci)

    clustering_coeff = sum(clusters) / len(clusters)
    return clustering_coeff

clustering_coefficient = get_clustering_coeff(G)

# The degree distribution P(k) of a network
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = collections.Counter(degree_sequence)
degrees, counts = zip(*degree_count.items())

fig, ax = plt.subplots()
plt.bar(degrees, counts, width=0.80, color="b")

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in degrees])
ax.set_xticklabels(degrees)

plt.show()

if nx.is_connected(G):
    diameter = nx.diameter(G, e=None, usebounds=False)
    print("Diameter is", diameter)

print("Number of Nodes:", nx.number_of_nodes(G))
print("Number of Edges:", nx.number_of_edges(G))
print("Average Degree:", avg_degree)
print("Density is", density)
print("The Clustering Coefficient of the graph is", clustering_coefficient)

'''
@inproceedings{nr-aaai15,
      title = {The Network Data Repository with Interactive Graph Analytics and Visualization},
      author={Ryan A. Rossi and Nesreen K. Ahmed},
      booktitle = {Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence},
      url={http://networkrepository.com},
      year={2015}
  }
'''