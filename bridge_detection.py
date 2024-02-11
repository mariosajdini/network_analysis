import networkx as nx
import matplotlib.pyplot as plt
# Example of creating a simple graph
G = nx.Graph()
# Add nodes and edges to your graph accordingly
G = nx.read_graphml('dataset_of_netwrok.graphml')
G = G.to_undirected()
bridges = list(nx.bridges(G))
print("Bridges in the network:", len(bridges))
def find_local_bridges(G):
    local_bridges = []
    for u, v in G.edges():
        # A local bridge has no common neighbors
        if not set(G.neighbors(u)).intersection(G.neighbors(v)):
            local_bridges.append((u, v))
    return local_bridges

local_bridges = find_local_bridges(G)
print("Local bridges in the network:", len(local_bridges))

pos = nx.spring_layout(G)  # positions for all nodes

# Draw the nodes and the edges (excluding bridges and local bridges)
nx.draw_networkx_nodes(G, pos)
normal_edges = [e for e in G.edges() if e not in bridges and e not in local_bridges]
nx.draw_networkx_edges(G, pos, edgelist=normal_edges)

# Draw bridges with a distinct color
nx.draw_networkx_edges(G, pos, edgelist=bridges, edge_color='r', width=2)

# Draw local bridges with another distinct color
nx.draw_networkx_edges(G, pos, edgelist=local_bridges, edge_color='b', width=2)

nx.draw_networkx_labels(G, pos)
plt.show()


