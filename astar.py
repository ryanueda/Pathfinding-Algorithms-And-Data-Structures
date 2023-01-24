import networkx as nx
from Node import Node

class astar():
    def __init__(self, start, finish, walls, boxes):
        #### CREATE NEW CLASS FOR THIS ####
        self.start = start
        self.finish = finish
        self.walls = walls
        self.boxes = boxes
        self.G = nx.Graph()

    def setup(self):
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes)):
                if i != j:
                    horizontal_distance = abs(self.boxes[i][0] - self.boxes[j][0])
                    vertical_distance = abs(self.boxes[i][1] - self.boxes[j][1])

                    if (horizontal_distance == 24 and vertical_distance == 0) or (horizontal_distance == 0 and vertical_distance == 24):
                        self.G.add_edge(self.boxes[i], self.boxes[j])


        for i in range(len(self.start)):
            for j in range(len(self.boxes)):
                horizontal_distance = abs(self.start[i][0] - self.boxes[j][0])
                vertical_distance = abs(self.start[i][1] - self.boxes[j][1])

                if (horizontal_distance == 24 and vertical_distance == 0) or (horizontal_distance == 0 and vertical_distance == 24):
                        self.G.add_edge(self.start[i], self.boxes[j])


        for i in range(len(self.finish)):
            for j in range(len(self.boxes)):
                horizontal_distance = abs(self.finish[i][0] - self.boxes[j][0])
                vertical_distance = abs(self.finish[i][1] - self.boxes[j][1])

                if (horizontal_distance == 24 and vertical_distance == 0) or (horizontal_distance == 0 and vertical_distance == 24):
                        self.G.add_edge(self.finish[i], self.boxes[j])

        self.path = nx.astar_path(self.G, self.start[0], self.finish[0])
        print(self.path)
        results = self.move()
        return results

    def move(self):
        start_node = Node(None, self.start[0])
        start_node.g = start_node.h = start_node.f = 0
        
        end_node = Node(None, self.finish[0])
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:
            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

                # Pop current off open list, add to closed list
                open_list.pop(current_index)
                closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Generate children
            children = []
            for new_position in self.G.neighbors(current_node.position): 
                # Create new node
                new_node = Node(current_node, new_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 24
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)