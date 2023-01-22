from turtle import Turtle

class Maze(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.pensize("gray")
        self.penup()
        self.speed(0)
        self.ht()