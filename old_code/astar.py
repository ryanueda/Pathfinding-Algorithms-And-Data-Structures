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

        # self.path = nx.astar_path(self.G, self.start[0], self.finish[0])
        # print(self.path)
        results = self.move()
        return results

    def min(self, items):
        best_item = []
        best_f = 0
        for item in items:
            if best_item is None or item.f < best_f:
                best_f = item.f
                best_item.append(item)
            elif item.f == best_f:
                best_item.append(item)
        
        if len(best_item) == 1:
            return best_item[0]
        return best_item

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
        # while len(open_list) > 0:
        while len(open_list) > 0:
            # Get the current node
            # for i in open_list:
            #     print(f'gay {i.position} {i.f}')
            # for r in closed_list:
            #     print(f'closed {r.position}')
            # current_node = self.min(open_list)
            
            current_node = min(open_list, key = lambda x: x.f)
            open_list.remove(current_node)
            closed_list.append(current_node)

            # Found the goal
            # print(current_node.position, end_node.position)
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                reversed_path = path[::-1]
                return reversed_path[1:] # Return reversed path

            # Generate children
            children = []
            
            # print(f'current {current_node.position}, new {list(self.G.neighbors(current_node.position))}')

            for new_position in list(self.G.neighbors(current_node.position)): 
                # Create new node
                new_node = Node(current_node, new_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + 24
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                    continue

                # Add the child to the open list
                open_list.append(child)