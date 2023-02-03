from Building import Building
from Endpoint import Endpoint
from Sprite import Sprite
import turtle
import time, sys
import networkx as nx
import os

class Maze():
    def __init__(self):
        pass

    def setupMaze(self, grid):
        for y in range(len(grid)):                       # select each line in the grid
            for x in range(len(grid[y])):                # identify each character in the line
                character = grid[y][x]                   # assign the grid reference to the variable character
                screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
                screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

                if character == "X":                     # if grid character contains an +
                    self.maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                    self.maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                    
                    # self.maze.setposition(screen_x - 12, screen_y + 12)
                    # self.maze.pendown()
                    # self.maze.color('black')
                    # for i in range(4):
                    #     # self.maze.goto(screen_x - 24, screen_y)
                    #     self.maze.forward(23)
                    #     self.maze.right(90)
                    # self.maze.color('gray')
                    # self.maze.penup()
                    
                    self.walls.append((screen_x, screen_y))   # add coordinate to walls list

                if character == "e":                     # if grid character contains an e
                    self.end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                    self.end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                    
                    # self.maze.setposition(screen_x - 12, screen_y + 12)
                    # self.maze.pendown()
                    # self.maze.color('black')
                    # for i in range(4):
                    #     # self.maze.goto(screen_x - 24, screen_y)
                    #     self.maze.forward(23)
                    #     self.maze.right(90)
                    # self.maze.color('gray')
                    # self.maze.penup()
                    
                    self.finish.append((screen_x, screen_y))  # add coordinate to finish list

                if character == "s":                     # if the grid character contains an s
                    self.end.goto(screen_x, screen_y)
                    self.end.stamp()
                    self.sprite.goto(screen_x, screen_y)      # move turtle to the x and y location

                    # self.maze.setposition(screen_x - 12, screen_y + 12)
                    # self.maze.pendown()
                    # self.maze.color('black')
                    # for i in range(4):
                    #     # self.maze.goto(screen_x - 24, screen_y)
                    #     self.maze.forward(23)
                    #     self.maze.right(90)
                    # self.maze.color('gray')
                    # self.maze.penup()

                    start = (screen_x, screen_y)
                    self.start.append((screen_x, screen_y))
                
                if character == ".":

                    # self.maze.setposition(screen_x - 12, screen_y + 12)
                    # self.maze.pendown()
                    # self.maze.color('black')
                    # for i in range(4):
                    #     # self.maze.goto(screen_x - 24, screen_y)
                    #     self.maze.forward(23)
                    #     self.maze.right(90)
                    # self.maze.color('gray')
                    # self.maze.penup()

                    self.boxes.append((screen_x, screen_y))