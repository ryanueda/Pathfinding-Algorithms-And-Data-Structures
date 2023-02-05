from Maze import Maze

class LeftHand(Maze):
    def __init__(self):
        super().__init__()
    
    def neighbors(self, node, direction):
        # Define directions
        if direction == 'up':
            directions = {'left': (-24, 0), 'up': (0, 24), 'right': (24, 0), 'down': (0, -24)}
        elif direction == 'right':
            directions = {'left': (0, 24), 'up': (24, 0), 'right': (0, -24), 'down': (-24, 0)}
        elif direction == 'down':
            directions = {'left': (24, 0), 'up': (0, -24), 'right': (-24, 0), 'down': (0, 24)}
        elif direction == 'left':
            directions = {'left': (0, -24), 'up': (-24, 0), 'right': (0, 24), 'down': (24, 0)}

        # Create empty dictionary to store neighbors in each direction
        neighbors_in_direction = {direction: None for direction in directions}
        neighbors = list(self.G.neighbors(node))

        # Iterate over directions
        for direction, offset in directions.items():
            # Get x and y coordinates of current node
            x, y = node

            # Get x and y coordinates of neighbor in the current direction
            x_offset, y_offset = offset
            neighbor = (x + x_offset, y + y_offset)
            
            # Check if the neighbor is in the list of neighbors of the current node
            if neighbor in neighbors:
                neighbors_in_direction[direction] = neighbor

        return neighbors_in_direction
    
    def pathfinding(self):
        path = []
        current_node = self.start[0]
        current_direction = 'up'
        directions = ['up', 'left', 'down', 'right']

        while current_node != self.finish[0]:
            # Get neighbors in each direction
            neighbors = self.neighbors(current_node, current_direction)
            faceindex = directions.index(current_direction)

            # Follows LHR priority rule - left, up, right, down
            if neighbors['left'] is not None:
                current_node = neighbors['left']
                path.append(neighbors['left'])

                if faceindex == len(directions) - 1:    # If current direction is right, then next direction is up
                    current_direction = directions[0]
                else:
                    current_direction = directions[faceindex + 1]
            
            elif neighbors['up'] is not None:   # Up is always the next direction
                current_node = neighbors['up']
                path.append(neighbors['up'])
            
            elif neighbors['right'] is not None:
                current_node = neighbors['right']
                path.append(neighbors['right'])

                if faceindex == 0: # If current direction is up, then next direction is right
                    current_direction = directions[-1]
                else:
                    current_direction = directions[faceindex - 1]

            elif neighbors['down'] is not None:
                current_node = neighbors['down']
                path.append(neighbors['down'])

                if faceindex + 2 > len(directions) - 1: # If current direction is right, then next direction is left, if current direction is down, the next direction is up
                    current_direction = directions[faceindex - 2]
                else:
                    current_direction = directions[faceindex + 2]
            
            if current_node == self.start[0]:   # If the current node is the start node, then the path is not valid
                path.append(False)
                break
        
        return path

    def moveSprite(self, results, solver):
        super().moveSprite(results, solver)

    def clearSprite(self):
        self.sprite.clear()
        self.sprite.goto(self.start[0])
        self.sprite.pendown()