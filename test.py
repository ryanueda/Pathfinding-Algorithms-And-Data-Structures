import turtle
import networkx as nx

# Create a maze graph using NetworkX
maze = nx.Graph()
# add nodes of the grid
for i in range(1, 26):
    maze.add_node(i)

# add edges between the nodes
maze.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 7), (4, 5), (5, 6), (6, 9), (6, 7), (7, 8), (8, 12), (8, 9),
                     (9, 10), (10, 13), (10, 11), (11, 12), (12, 15), (12, 13), (13, 14), (14, 17), (14, 15),
                     (15, 16), (16, 19), (16, 17), (17, 18), (18, 21), (18, 19), (19, 20), (20, 23), (20, 21),
                     (21, 22), (22, 24), (22, 25), (25, 24)])

# Create a turtle object
t = turtle.Turtle()

# Set the initial position of the turtle to the start of the maze
t.setpos(-200, 200)

# Set the current node to the start of the maze
current_node = 1

# Use the left-hand rule to move through the maze
while current_node != 25:
    next_nodes = list(maze.neighbors(current_node))
    left_node = None
    for next_node in next_nodes:
        if next_node < current_node:
            left_node = next_node
            break
    if left_node is None:
        for next_node in next_nodes:
            if next_node > current_node:
                left_node = next_node
                break
    current_node = left_node
    t.forward(40)
    t.left(90)

turtle.done()
