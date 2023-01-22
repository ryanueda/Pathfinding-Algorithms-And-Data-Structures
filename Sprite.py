from turtle import Turtle
class Sprite(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)              # point turtle to point down
        self.penup()
        self.speed(0)

    # def spriteDown(self):
    #     if (self.heading() == 270):                   # check to see if the sprite is pointing down
    #         x_walls = round(sprite.xcor(),0)          # sprite x coordinates =
    #         y_walls = round(sprite.ycor(),0)
    #         if (x_walls, y_walls) in finish:          # if sprite and the
    #             print("Finished")
    #             endProgram()
    #         if (x_walls +24, y_walls) in walls:          # check to see if they are walls on the left
    #             if(x_walls, y_walls -24) not in walls:   # check to see if path ahead is clear
    #                 self.forward(24)
    #             else:
    #                 self.right(90)
    #         else:
    #             self.left(90)
    #             self.forward(24)


    # def spriteLeft(self):
    #     if (self.heading() == 0):
    #         x_walls = round(sprite.xcor(),0)
    #         y_walls = round(sprite.ycor(),0)
    #         if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
    #             print("Finished")
    #             endProgram()
    #         if (x_walls, y_walls +24) in walls:       # check to see if they are walls on the left
    #             if(x_walls +24, y_walls) not in walls:
    #                 self.forward(24)
    #             else:
    #                 self.right(90)
    #         else:
    #             self.left(90)
    #             self.forward(24)


    # def spriteUp(self):
    #     if (self.heading() == 90):
    #         x_walls = round(sprite.xcor(),0)
    #         y_walls = round(sprite.ycor(),0)
    #         if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
    #             print("Finished")
    #             endProgram()
    #         if (x_walls -24, y_walls ) in walls:  # check to see if they are walls on the left
    #             if (x_walls, y_walls + 24) not in walls:
    #                 self.forward(24)
    #             else:
    #                 self.right(90)
    #         else:
    #             self.left(90)
    #             self.forward(24)

    # def spriteRight(self):
    #     if (self.heading() == 180):

    #         x_walls = round(sprite.xcor(),0)
    #         y_walls = round(sprite.ycor(),0)
    #         if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
    #             print("Finished")
    #             endProgram()
    #         if (x_walls, y_walls -24) in walls:  # check to see if they are walls on the left
    #             if (x_walls - 24, y_walls) not in walls:
    #                 self.forward(24)
    #             else:
    #                 self.right(90)
    #         else:
    #             self.left(90)
    #             self.forward(24)