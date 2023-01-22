from Maze import Maze
from End import End
from Sprite import Sprite
# from turtle import Turtle, Screen
import turtle
import time, sys

screen = turtle.Screen() # Define turtle screen
screen.bgcolor('white')
screen.setup(1300, 700) # Dimension of working window
TURTLE_SIZE = 20

class Main(turtle.Turtle):
    def __init__(self):
        self.maze = Maze()
        self.sprite = Sprite()
        self.end = End()
        self.walls = []
        self.finish = []

    def fileio(self):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2.2 - TURTLE_SIZE/2)
        turtle.write('Please enter file name on terminal ', font=("Verdana", 10, "normal"))
        turtle.penup()

        while True:
            # filepath = input('Enter filename: ')
            filepath = 'city_map'
            filename = open(f'dsaa/{filepath}')
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

        print('Passed validation')
        turtle.clear()
        turtle.write('PIZZA RUNNERS: Done by Wee Leong & Ryan DAAA/FT/2B/05', font=("Verdana", 10, "normal"))
        turtle.ht()
        self.setupMaze(grid)
    
    def setupMaze(self, grid):
        for y in range(len(grid)):                       # select each line in the grid
            for x in range(len(grid[y])):                # identify each character in the line
                character = grid[y][x]                   # assign the grid reference to the variable character
                screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
                screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

                if character == "X":                     # if grid character contains an +
                    self.maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                    self.maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                    self.walls.append((screen_x, screen_y))   # add coordinate to walls list

                if character == "e":                     # if grid character contains an e
                    self.end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                    self.end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                    self.finish.append((screen_x, screen_y))  # add coordinate to finish list

                if character == "s":                     # if the grid character contains an s
                    self.sprite.goto(screen_x, screen_y)      # move turtle to the x and y location

main = Main()
main.fileio()
screen.exitonclick()