from turtle import Turtle
class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)              # point turtle to point down
        self.penup()
        # self.speed(3)