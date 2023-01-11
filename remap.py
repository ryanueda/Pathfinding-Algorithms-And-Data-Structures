import turtle
import time
import sys

# define and setup screen
screen = turtle.Screen()               # define the turtle screen
screen.bgcolor("white")                # set the background colour
screen.setup(1300,700)                 # setup the dimensions of the working window

TURTLE_SIZE = 20
turtle.penup()
turtle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2.2 - TURTLE_SIZE/2)
turtle.write('PIZZA RUNNERS: Done by Wee Leong & Ryan DAAA/FT/2B/05', font=("Verdana", 10, "normal"))
turtle.penup()


# class for Maze (white square)
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("gray")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # sets the speed that the maze is written to the screen

# Class for End marker (green square)
class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

# class for turtle sprite (red turtle)
class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)              # point turtle to point down
        self.penup()
        self.speed(0)


    def spriteDown(self):
        if (self.heading() == 270):                   # check to see if the sprite is pointing down
            x_walls = round(sprite.xcor(),0)          # sprite x coordinates =
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:          # if sprite and the
                print("Finished")
                endProgram()
            if (x_walls +24, y_walls) in walls:          # check to see if they are walls on the left
                if(x_walls, y_walls -24) not in walls:   # check to see if path ahead is clear
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteLeft(self):
        if (self.heading() == 0):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls +24) in walls:       # check to see if they are walls on the left
                if(x_walls +24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteUp(self):
        if (self.heading() == 90):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls -24, y_walls ) in walls:  # check to see if they are walls on the left
                if (x_walls, y_walls + 24) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)

    def spriteRight(self):
        if (self.heading() == 180):

            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls -24) in walls:  # check to see if they are walls on the left
                if (x_walls - 24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


def endProgram():
    screen.exitonclick()
    sys.exit()


# grid = [
# "++++++++++++++++++++++++++++++++++++++++++++++",
# "+ s             +                            +",
# "+  ++++++++++  +++++++++++++  +++++++  ++++  +",
# "+           +                 +        +     +",
# "+  +++++++  +++++++++++++  +++++++++++++++++++",
# "+  +     +  +           +  +                 +",
# "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +",
# "+  +  +  +  +  +  +     +  +  +  +        +  +",
# "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  +",
# "+  +     +  +              +           +  +  +",
# "+  ++++  +  ++++++++++++++++  +++++++++++++  +",
# "+     +  +                    +              +",
# "++++  +  ++++++++++++++++++++++  ++++++++++  +",
# "+  +  +                    +     +     +  +  +",
# "+  +  ++++  +++++++++++++  +  ++++  +  +  +  +",
# "+  +  +     +     +     +  +  +     +     +  +",
# "+  +  +  +++++++  ++++  +  +  +  ++++++++++  +",
# "+                       +  +  +              +",
# "++++  +  +  ++++++++++  +  +  +  +++++++++++++",
# "+++++++++++++++++++++++e++++++++++++++++++++++",
# ]

grid = [
    "XXXXXXXXXXXX",
    "X...X..X..eX",
    "X.X....X.XXX",
    "X..X.X.X.X.X",
    "XX.XXX.X...X",
    "X........X.X",
    "XsXX...X...X",
    "XXXXXXXXXXXX"
]


def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid
        for x in range(len(grid[y])):                # identify each character in the line
            character = grid[y][x]                   # assign the grid reference to the variable character
            screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
            screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

            if character == "X":                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))   # add coordinate to walls list

            if character == "e":                     # if grid character contains an e
                end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if character == "s":                     # if the grid character contains an s
                sprite.goto(screen_x, screen_y)      # move turtle to the x and y location
                sprite.stamp()



################# PROGRAM STARTS HERE #################
while True:
    filename = input('Enter filename: ')
    filename = open(filename)
    content = filename.read()
    grid = content.split('\n')

    for line in range(len(grid)):
        row = grid[line]

        # check for equal number of rows
        if len(row) != len(grid[0]):
            print('Invalid File Format: unequal number of characters per line')
            continue

        # check for invalid characters in file
        for char in range(len(row)):
            if row[char] not in ['X', '.', 's', 'e']:
                print("Invalid File Format: Maze has invalid characters")

        # check if vertical borders are all "X"
        if row[0] != "X" or row[-1] != "X":
            print("Invalid File Format: Maze has incomplete borders")
            continue

    # check if horizontal borders are all "X"
    if set(grid[0]) != {"X"} or set(grid[-1]) != {"X"}:
        print("Invalid File Format: Maze has incomplete borders")
        continue

    break

maze = Maze()                # instantiate Maze class
sprite = sprite()            # instantiate Sprite class
end = End()                  # instantiate End class
walls = []                    # create empty list to store wall coordinates
finish = []                  # create finish array

setupMaze(grid)              # call function to setup maze grid

# demo on key press function
def altAlgo():
    turtle.forward(10)

while True:
    turtle.onkey(altAlgo, 'Right')
    turtle.listen()
    sprite.spriteRight()
    sprite.spriteDown()
    sprite.spriteLeft()
    sprite.spriteUp()

    time.sleep(0.02)