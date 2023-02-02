from Building import Maze
from Start_End import End
from Sprite import Sprite
import turtle
import time, sys
# from old_code.lefthand import LeftHand
# from old_code.astar import astar
import os

TURTLE_SIZE = 20

class Main(turtle.Turtle):
    def __init__(self):
        self.screen = turtle.Screen() # Define turtle screen
        self.screen.setup(1300, 700) # Dimension of working window

