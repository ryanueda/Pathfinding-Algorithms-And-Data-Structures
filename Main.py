import turtle
from Button import Button
from FileIO import FileIO
from Maze import Maze
from LeftHand import LeftHand
from Astar import astar

class Nav(turtle.Turtle):
    def __init__(self): # Calls Turtle, Button, and Main classes
        super().__init__()

        self.len_x = 300 # Length of button
        self.len_y = 100 # Height of button
        self.x = self.len_x * 1.65 - self.screen.window_width()/2   # Coordinates of button
        self.y = self.len_y * 3 - self.screen.window_height()/2  # Coordinates of button
        self.current_solver = 'lh'

        self.button = Button(self.len_x, self.len_y)
        self.fileio = FileIO()
        self.maze = Maze()
        self.lefthand = LeftHand()
        self.astar = astar()

    def run(self):
        self.screen.setup(1300, 700) # Dimension of working window

        self.ht() # Hide turtle cursor
        self.penup() # Lift the pen, so it doesn't leave a trail when moving
        self.sety(100) # Move turtle to y = 100
        self.write("Welcome to Pizza Runners!", align="center", font = ("Arial", 30, "normal"))
    
        self.button.draw_button(self.x, self.y, '[Start]', 'black', 'white', self.map)


    def map(self, x, y):
        if x > self.x and x < (self.x + self.len_x) and y > self.y and y < (self.y + self.len_y):   # Ensure the button is clicked and ignore clicks outside the button
            turtle.onscreenclick(None)
            self.button.clear()
            self.clear()
            
            self.fileio.validation()

            self.goto(40/2 - self.screen.window_width()/2, self.screen.window_height()/2.2 - 20/2)
            self.write('PIZZA RUNNERS: Done by Wee Leong & Ryan DAAA/FT/2B/05', font=("Verdana", 10, "normal"))

            self.maze.setupMaze(self.fileio.getgrid(), (60/2 - self.screen.window_width()/2, self.screen.window_height()/2.2 - 60/2))
            self.maze.setupAlgo()

            self.algo()
            turtle.onkey(self.algo, 'Tab')

    def algo(self):
        if self.current_solver == 'lh':
            turtle.onkey(None, 'Tab')   # Disable the Tab key. This is to prevent the user from spamming the Tab key and causing the program to crash or act weirdly

            self.astar.clearSprite()

            result = self.lefthand.pathfinding()

            if result[-1] == False:
                self.goto(400/2 - self.screen.window_width()/2, self.screen.window_height()/2.2 - (250))
                self.color('red')
                self.write('Unable to find exit', align="center", font = ("Arial", 15, "bold"))
                return

            self.lefthand.moveSprite(result, 'Left Hand')

            self.current_solver = 'astar'   # Ensure that the next time the Tab key is pressed, the other algorithm will be used
            turtle.onkey(self.algo, 'Tab') # Re-enable the Tab key
        
        elif self.current_solver == 'astar':
            turtle.onkey(None, 'Tab')   # Disable the Tab key. This is to prevent the user from spamming the Tab key and causing the program to crash or act weirdly

            self.lefthand.clearSprite()

            result = self.astar.pathfinding()

            if result[-1] == False:
                self.goto(320/2 - self.screen.window_width()/2, self.screen.window_height()/2.2 - (250))
                self.color('red')
                self.write('Unable to find exit', align="center", font = ("Arial", 15, "bold"))
                return

            self.astar.moveSprite(result, 'A*') 

            self.current_solver = 'lh' # Ensure that the next time the Tab key is pressed, the other algorithm will be used
            turtle.onkey(self.algo, 'Tab') # Re-enable the Tab key


if __name__ == '__main__':
    nav = Nav()
    nav.run()
    turtle.done()