import networkx as nx

# Load the graph
G = nx.read_graphml('dataset_of_netwrok.graphml')
G = G.to_undirected()

transitivity = nx.transitivity(G)
print("Transitivity of the Graph:", transitivity)

