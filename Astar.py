from Maze import Maze
from Node import Node
from Minheap import MinHeap

class astar(Maze):
    def __init__(self):
        super().__init__()
        self.minheap = MinHeap()

    def pathfinding(self):
        path = []

        start_node = Node(None, self.start[0])
        start_node.g = start_node.h = start_node.f = 0

        end_node = Node(None, self.finish[0])
        end_node.g = end_node.h = end_node.f = 0
        
        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until the end
        self.minheap.clear()

        while len(open_list) > 0:
            for node in open_list:
                self.minheap.insert(node)
            
            current_node = self.minheap.extract_min()

            # current_node is being read, so remove it from the open list
            open_list.remove(current_node)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                path.reverse()
                return path[1:] # Return reversed path
            
            if current_node == start_node and len(open_list) != 0:
                path.append(False)
                return path

            # Generate new possible neighbor
            new_neighbor = []

            for new_position in list(self.G.neighbors(current_node.position)):
                # Get node object
                new_node = Node(current_node, new_position)

                # Append
                new_neighbor.append(new_node)
            
            # Loop through new neighbors and add to open list if condition is met
            for neighbor in new_neighbor:
                # Check if new neighbor has already been explored 
                if len([closed_neighbor for closed_neighbor in closed_list if closed_neighbor == neighbor]) > 0:
                    continue

                # Create new g, h, and f values
                neighbor.g = current_node.g + 24
                neighbor.h = ((neighbor.position[0] - end_node.position[0]) ** 2) + ((neighbor.position[1] - end_node.position[1]) ** 2)
                neighbor.f = neighbor.g + neighbor.h

                # Check if new path is already in the open list, to be explored
                if len([open_node for open_node in open_list if neighbor == open_node]) > 0:
                    continue

                # Add the path to the open list since all conditions are met
                open_list.append(neighbor)

    def moveSprite(self, results, solver):
        super().moveSprite(results, solver)

    def clearSprite(self):
        self.sprite.clear()
        self.sprite.goto(self.start[0])
        self.sprite.pendown()