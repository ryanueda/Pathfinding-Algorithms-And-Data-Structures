import networkx as nx

class LeftHand():
    def __init__(self, start, finish, walls, boxes):
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

    def move(self):
        path = []
        d = []
        current_node = self.start[0]
        direction = 'up'
        while True:
            neighbors = self.neighbors(current_node, direction)

            if neighbors['left'] is not None:
                current_node = neighbors['left']
                path.append(neighbors['left'])

                if direction == 'up':
                    direction = 'left'
                    d.append('left')

                elif direction == 'right':
                    direction = 'up'
                    d.append('up')

                elif direction == 'down':
                    direction = 'right'
                    d.append('right')

                elif direction == 'left':
                    direction = 'down'
                    d.append('down')

            elif neighbors['up'] is not None:
                current_node = neighbors['up'] 
                path.append(neighbors['up'])

                if direction == 'up':
                    d.append('up')

                elif direction == 'right':
                    d.append('right')
                    
                elif direction == 'down':
                    d.append('down')

                elif direction == 'left':
                    d.append('left')

            elif neighbors['right'] is not None:
                current_node = neighbors['right']
                path.append(neighbors['right'])

                if direction == 'up':
                    direction = 'right'
                    d.append('right')

                elif direction == 'right':
                    direction = 'down'
                    d.append('down')

                elif direction == 'down':
                    direction = 'left'
                    d.append('left')

                elif direction == 'left':
                    direction = 'up'
                    d.append('up')

            elif neighbors['down'] is not None:
                current_node = neighbors['down']
                path.append(neighbors['down'])

                if direction == 'up':
                    direction = 'down'
                    d.append('down')

                elif direction == 'right':
                    direction = 'left'
                    d.append('left')

                elif direction == 'down':
                    direction = 'up'
                    d.append('up')
                    
                elif direction == 'left':
                    direction = 'right'
                    d.append('right')

            if current_node == self.finish[0]:
                print('REACHED!!!')
                break

        return path, d