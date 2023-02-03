import turtle
from Button import Button
from old_code.test import Main

class Nav(turtle.Turtle):
    def __init__(self): # Calls Turtle, Button, and Main classes
        super().__init__()
        self.button = Button(self)
        self.main = Main()

    def run(self):
        self.screen.setup(1300, 700) # Dimension of working window

        self.ht() # Hide turtle cursor
        self.penup() # Lift the pen, so it doesn't leave a trail when moving
        self.sety(100) # Move turtle to y = 100
        self.write("Welcome!", align="center", font = ("Arial", 30, "normal"))
    
        self.button.draw_button(-400, -100, '[Start]', 'black', 'white', self.main.fileio)
        # self.clear()


if __name__ == '__main__':
    nav = Nav()
    nav.run()
    turtle.done()