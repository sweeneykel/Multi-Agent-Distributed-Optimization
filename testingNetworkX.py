import networkx as nx

from Node import Node

T = nx.Graph()

one = Node(1, 10)
T.add_node(one)
two = Node(2, 20)
T.add_node(two)
three = Node(3, 30)
T.add_node(three)

#G.add_edge(n1,n2, object=x)
#n1, n2: protein objects from Protein Databank
#x = XML record of interaction between n1 and n2
T.add_edge(one, two)
T.add_edge(one, three)

# iterate through all neighbors of one
#for j in T.neighbors(one):
    #print(type(j.index))

# show the graph
#nx.draw(G)
#plt.show()

#print(T.number_of_nodes())
#print(T.number_of_edges())
#print(type(G.nodes)) #<class 'networkx.classes.reportviews.NodeView'>
#for n in list(T.nodes):
 #   print("!!", n.index)

print("Reassign values at x_i_pko to x_i_k")
for n in list(T.nodes):
    print('index k was originally: ', n.x_i_k)
    n.x_i_k = n.x_i_kpo
    print('index k is now: ', n.x_i_k)
    print('index k plus 1: ', n.x_i_kpo)

print("Increment x_i_kpo")
q = 1
for n in list(T.nodes):
    print('index k is: ', n.x_i_k)
    print('index k plus 1 was originally: ', n.x_i_kpo)
    n.x_i_kpo += q
    print('index k is: ', n.x_i_k)
    print('index k plus 1 is now: ', n.x_i_kpo)
    q += 1

print("Reassign values at x_i_pko to x_i_k")
for n in list(T.nodes):
    print('index k was originally: ', n.x_i_k)
    n.x_i_k = n.x_i_kpo
    print('index k is now: ', n.x_i_k)
    print('index k plus 1: ', n.x_i_kpo)




