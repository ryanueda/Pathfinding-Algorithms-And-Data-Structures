import turtle

# Create turtle named t
t = turtle.Turtle()

# Create window
screen = turtle.Screen()
TURTLE_SIZE = 20

# Fastest turtle speed
t.speed(0)

# top-left
t.hideturtle()
t.penup()
t.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2.2 - TURTLE_SIZE/2)
t.showturtle()
t.pendown()

t.write('PIZZA RUNNERS: Done by Wee Leong & Ryan DAAA/FT/2B/05', font=("Verdana", 10, "normal"))
t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

def drawSquare(color, length1=30, length2=30):
    t.color('black', color)
    t.begin_fill()
    for i in range(2):
        t.forward(length1)
        t.left(90)
        t.forward(length2)
        t.left(90)
    t.end_fill()

def nextSquare():
    t.penup()
    t.forward(30)
    t.pendown()

def newRow():
    t.penup()
    t.backward(30*len(row))
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()

city_map = [
    "XXXXXXXXXXXX",
    "X...X..X..eX",
    "X.X....X.XXX",
    "X..X.X.X.X.X",
    "XX.XXX.X...X",
    "X........X.X",
    "XsXX...X...X",
    "XXXXXXXXXXXX",
]

## read in file
filepath = 'dsaa/city_map'
filepath = open(filepath)
content = filepath.read()
content = content.split('\n')

## draw map in turtle
for i in range(len(content)):
    row = content[i]
    for letter in range(len(row)):
        if row[letter] == 'X':
            drawSquare('gray')
            nextSquare()
        elif row[letter] == '.':
            drawSquare('white')
            nextSquare()
        elif row[letter] == 'e':
            drawSquare('cyan')
            nextSquare()
        elif row[letter] == 's':
            drawSquare('pale green')
            nextSquare()

    newRow()
        
screen.mainloop()