
from Node import Node
import networkx as nx

from primalUpdate import primalUpdate
from dualUpdate import dualUpdate

# initialize indexing

# create graph
G = nx.Graph()

# add nodes
one = Node(1,0)
G.add_node(one)
two = Node(2,0)
G.add_node(two)
three = Node(3,0)
G.add_node(three)

# add edges
G.add_edge(one, two)
G.add_edge(one, three)

# Begin Distributed Optimization
# for all nodes in Graph: Calculate Primal Update
for n in list(G.nodes):
    print(n.index)
    # primalUpdate(n)
    # return x_i_kplus1

# for all nodes in Graph: "Transmit" Primal Update
# I don't know if this actually needs to be done since we know who the
# neighbors are and we can access j.x_i_kpo

# for all nodes in Graph: Calculate Dual Update
for n in list(G.nodes):
    print(n.index)
    # dualUpdate(n)
    # return y_i_kplus1

# update k
for n in list(G.nodes):
    n.x_i_k = n.x_i_kpo

# repeat until stopping criteria is met

