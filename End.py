from turtle import Turtle

class End(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.ht()