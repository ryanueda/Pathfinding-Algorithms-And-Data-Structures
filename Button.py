import turtle
# from old_code.test import Main

screen = turtle.Screen()
screen.setup(1300, 700)

class Button(turtle.Turtle):
    # Call the parent turtle class
    def __init__(self, len_x = 300, len_y = 100):
        super().__init__()
        self.speed(0)
        
        self.len_x = len_x
        self.len_y = len_y

    # Code required to draw a button
    def draw_button(self, x, y, text, color = 'black', text_color = 'white', func = None):
        self.x = x
        self.y = y
        self.func = func

        self.ht() # Hide the turtle
        self.penup() # Lift the pen, so it doesn't leave a trail when moving
        self.goto(self.x, self.y)
        self.color(color) # Set the color of the button
        self.begin_fill() # Start filling the button created below with the color
        for i in range(2): # Draw a box from the bottom left corner. range(2) to draw a square, range(1) to draw a triangle
            self.forward(self.len_x)
            self.left(90)
            self.forward(self.len_y)
            self.left(90)
        self.end_fill()

        self.penup()
        self.goto(self.x + (self.len_x / 2), self.y + (self.len_y / 4)) # Move to the center of the button
        self.color(text_color) # Change color for text
        self.write(text, font=("Courier", "30", "bold"), align="center")

        if func == None:
            turtle.onscreenclick(self.button_click, 1) # Detect a click on the button
        
        else:
            # turtle.onscreenclick(self.non_default, 1)
            turtle.onscreenclick(func, 1)

    # Test if button works as expected
    def button_click(self, x, y):
        if x > self.x and x < (self.x + self.len_x) and y > self.y and y < (self.y + self.len_y):
            print('Button clicked')

    # def non_default(self, x, y):
    #     if x > self.x and x < (self.x + self.len_x) and y > self.y and y < (self.y + self.len_y):
    #         turtle.onscreenclick(None)
    #         self.clear()
    #         self.parent_turtle.clear()
    #         self.func()


# Test if the button class works as expected
# if __name__ == '__main__':
#     button = Button()
#     main2 = Main()
#     button.draw_button(-400, -100, 'hello', 'black', 'white', main2.fileio)
#     turtle.done()