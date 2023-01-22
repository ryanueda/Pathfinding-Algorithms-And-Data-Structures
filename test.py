import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5,1)])

path = []
current_node = 1
while len(path) < len(G.nodes()):
    path.append(current_node)
    next_nodes = list(G.neighbors(current_node))
    for next_node in next_nodes:
        if next_node not in path:
            current_node = next_node
            break

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the nodes
node_positions = {1: (0, 0), 2: (20, 0), 3: (40, 0), 4: (60, 0), 5: (80, 0)}
for node in G.nodes():
    t.dot()
    t.setpos(node_positions[node])

# Draw the edges
for i in range(len(path)-1):
    t.penup()
    t.goto(node_positions[path[i]])
    t.pendown()
    t.goto(node_positions[path[i+1]])

turtle.done()
