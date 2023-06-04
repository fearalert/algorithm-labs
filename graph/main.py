import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import collections

def import_graph(url):
    header_list = ["a", "b", "w", "y"]
    # E = pd.read_csv('D:\\algorithms-lab\\graph\\aves-songbird-social.edges', sep=" ", header=None, names=header_list)
    E = pd.read_csv(url, sep=" ", header=None, names=header_list)
    G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
    return G

def draw_graph(G):
    # Add numbers to the nodes
    node_labels = {node: str(node) for node in G.nodes()}
    # Draw the network with node labels
    nx.draw(G, with_labels=True, labels=node_labels)
    plt.show()

def get_average_deg(G):
    degrees = G.degree()
    avg_degree = sum(dict(degrees).values()) / G.number_of_nodes()
    return avg_degree

def get_density(E, N):
    density = (2 * E) / (N* (N - 1))
    return density

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

def get_diameter(G):
    if nx.is_connected(G):
        diameter = nx.diameter(G, e=None, usebounds=False)
        print("Diameter is", diameter)

def get_degree_distribution(G):
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


#Usage Code
url = 'D:\\algorithms-lab\\graph\\mammalia-voles-rob-trapping.edges'
# url = 'D:\\algorithms-lab\\graph\\aves-sparrow-social.edges'
Graph = import_graph(url)
E = Graph.number_of_edges()
N = Graph.number_of_nodes()
clustering_coefficient = get_clustering_coeff(Graph)
draw_graphs = draw_graph(Graph)
avg_degree = get_average_deg(Graph)
density = get_density(E, N)

get_degree_distribution(Graph)

get_diameter(Graph)

print("Number of Nodes:", nx.number_of_nodes(Graph))
print("Number of Edges:", nx.number_of_edges(Graph))
print("Average Degree:", avg_degree)
print("Density is", density)
print("The Clustering Coefficient of the graph is", clustering_coefficient, "/n")

'''
@inproceedings{nr-aaai15,
      title = {The Network Data Repository with Interactive Graph Analytics and Visualization},
      author={Ryan A. Rossi and Nesreen K. Ahmed},
      booktitle = {Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence},
      url={http://networkrepository.com},
      year={2015}
  }
'''
