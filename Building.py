from turtle import Turtle

class Building(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.color('gray')
        self.speed(0)
        self.ht()