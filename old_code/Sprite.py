from turtle import Turtle
class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("arrow")
        self.color("red")
        # self.setheading(270)              # point turtle to point down
        self.penup()
        self.shapesize(0.5, 0.5, 1)
        # self.speed(0)
        # self.ht()