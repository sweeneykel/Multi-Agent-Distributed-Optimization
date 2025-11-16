
from Node import Node
import networkx as nx

from primalUpdate import primalUpdate
from dualUpdate import dualUpdate

# initialize indexing



# create graph
G = nx.Graph()

# add nodes
one = Node(1)
G.add_node(one)
two = Node(2)
G.add_node(two)
three = Node(3)
G.add_node(three)

# add edges
G.add_edge(one, two)
G.add_edge(one, three)

# Begin Distributed Optimization
# for all nodes in Graph: Calculate Primal Update
for n in list(G.nodes):
    # primalUpdate(n)
    # return x_i_kplus1

# for all nodes in Graph: "Transmit" Primal Update



# for all nodes in Graph: Calculate Dual Update
for n in list(G.nodes):
    # dualUpdate(n)
    # return y_i_kplus1

# update k


# repeat until stopping criteria is met

