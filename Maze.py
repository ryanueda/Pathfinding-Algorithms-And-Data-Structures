from Building import Building
from Endpoint import Endpoint
from Sprite import Sprite
import networkx as nx
import turtle

class Maze(turtle.Turtle):
    __shared_state = {} # Use of Borg pattern to share the state of Maze class with Astar and LeftHand classes

    def __init__(self):
        self.__dict__ = self.__shared_state # Use of Borg pattern
        self.maze = Building()
        self.sprite = Sprite()
        self.endpoint = Endpoint()
        self.G = nx.Graph()

        self.walls = []
        self.start = []
        self.finish = []
        self.boxes = []

    def setupMaze(self, grid, coor):
        turtle.title('Setting up maze...')
        for y in range(len(grid)):                       # select each line in the grid
            for x in range(len(grid[y])):                # identify each character in the line
                character = grid[y][x]                   # assign the grid reference to the variable character

                screen_x = coor[0] + (x * 24)               # assign screen_x to screen starting position 
                screen_y = coor[1] - (y * 24)                # assign screen_y to screen starting position 

                if character == "X":                           # if grid character contains an +
                    self.maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                    self.maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                    
                    self.mazeborder(screen_x, screen_y)
                    
                    self.walls.append((screen_x, screen_y))    # add coordinate to walls list

                if character == "e":                               # if grid character contains an e
                    self.endpoint.goto(screen_x, screen_y)         # move turtle to the x and y location and
                    self.endpoint.stamp()                          # stamp a copy of the turtle (green square) on the screen
                    
                    self.mazeborder(screen_x, screen_y)

                    self.finish.append((screen_x, screen_y))       # add coordinate to finish list

                if character == "s":                          # if the grid character contains an s
                    self.sprite.st()                          # show the turtle on the screen
                    self.endpoint.goto(screen_x, screen_y)
                    self.endpoint.stamp()

                    self.mazeborder(screen_x, screen_y)

                    self.sprite.goto(screen_x, screen_y)      # move turtle to the x and y location

                    self.start.append((screen_x, screen_y))
                
                if character == ".":    # if the grid character contains a .
                    self.boxes.append((screen_x, screen_y))

                    self.mazeborder(screen_x, screen_y)

    def mazeborder(self, screen_x, screen_y):   # Creates a line border around each square
        self.maze.setposition(screen_x - 12, screen_y + 12)
        self.maze.pendown()
        self.maze.color('black')
        for i in range(4):
            # self.maze.goto(screen_x - 24, screen_y)
            self.maze.forward(23)
            self.maze.right(90)
        self.maze.color('gray')
        self.maze.penup()
    
    def setupAlgo(self):
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes)):
                if i != j:
                    horizontal_distance = abs(self.boxes[i][0] - self.boxes[j][0])  # Calculate horizontal distance between boxes
                    vertical_distance = abs(self.boxes[i][1] - self.boxes[j][1])    # Calculate vertical distance between boxes

                    if (horizontal_distance == 24 and vertical_distance == 0) or (horizontal_distance == 0 and vertical_distance == 24):   # 24 represents the width/height of each square
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

    def moveSprite(self, results, solver):
        steps = 0
        for result in range(len(results)):
            if self.sprite.position()[0] + 24 == results[result][0]:    # Determine next direction taken by sprite
                direction = 'right'
            elif self.sprite.position()[0] - 24 == results[result][0]:
                direction = 'left'
            elif self.sprite.position()[1] + 24 == results[result][1]:
                direction = 'up'
            elif self.sprite.position()[1] - 24 == results[result][1]:
                direction = 'down'

            # Follows this orientation 0 - east, 90 - north, 180 - west, 270 - south
            if direction == 'right':
                self.sprite.setheading(0)
            elif direction == 'left':
                self.sprite.setheading(180)
            elif direction == 'up':
                self.sprite.setheading(90)
            elif direction == 'down':
                self.sprite.setheading(270)

            steps += 1
            turtle.title(f'{solver} Maze Solver - {steps} steps')
            self.sprite.goto(results[result])

        self.sprite.penup()
            