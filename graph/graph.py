import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import collections

header_list = ["a","b","w"]
# header_list = ["a","b","w", "y"]
E = pd.read_csv('D:\\algorithms-lab\\graph\\aves-songbird-social.edges', sep= " ",header=None, names=header_list)

G = nx.from_pandas_edgelist(E,"a","b",["w"],)
nx.draw(G)

degrees = G.degree()

avg = sum([d for (n, d) in nx.degree(G)]) / float(G.number_of_nodes())

density = (2*float(G.number_of_edges()))/(float(G.number_of_nodes())*float(G.number_of_nodes()-1))

def getClusteringCoeff(G):
    clusters = []
    for node in G.nodes():
        neighbors = [neighbor for neighbor in G.neighbors(node)]
        ki = len(neighbors)
        subgraph = nx.subgraph(G, neighbors)
        ei = subgraph.number_of_edges()
        
        if ki!= 0 and ki!=1:
            ci = (2 * ei) / ( ki * (ki - 1))
        else:
            ci = 0
        clusters.append(ci)
    
    clusteringCoeff = sum(clusters) / len(clusters)
    return clusteringCoeff

clustering = getClusteringCoeff(G)

#The degree distribution P(k) of a network
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color="b")

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

plt.show()

if nx.is_connected(G) == True:
    diameter = nx.diameter(G, e=None, usebounds=False)
    print("Diameter is ",diameter)

print("Number of Nodes",nx.number_of_nodes(G))
print("Number of Edges",nx.number_of_edges(G))
print("Number of average Degree",avg)
print("Density is ",density)
print("The Clustering Coefficient of the graph is ",clustering)

'''
@inproceedings{nr-aaai15,
      title = {The Network Data Repository with Interactive Graph Analytics and Visualization},
      author={Ryan A. Rossi and Nesreen K. Ahmed},
      booktitle = {Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence},
      url={http://networkrepository.com},
      year={2015}
  }
'''