import turtle
import os 
from Maze import Maze

class FileIO():
    def __init__(self):
        self.maze = Maze()
        turtle.screensize(1300, 700)

    def validation(self):
        filepath = turtle.textinput('Enter File', 'Enter File Name Below:')     # Uses Turtle to get input from user
        while True:
            
            # filepath = 'city_map'   # NOTE: FOR TESTING ONLY
            
            try:    # ensures that input filepath regardless of directory or folder
                cwd = os.getcwd()
                for root, dirs, files in os.walk(cwd):
                    for file in files:
                        if file == filepath:
                            filepath = os.path.join(root, file)
            except:
                print('Unknown Error')

            try:    # catch errors if file does not exist/empty input
                filename = open(filepath)
            except FileNotFoundError or PermissionError:
                print('File not present in directory')
                filepath = turtle.textinput('Invalid File Name', 'Enter File Name Below:')
                continue

            content = filename.read()
            grid = content.split('\n')
            turtle.title('Checking File Format...')

            for line in range(len(grid)):
                row = grid[line]

                # check for equal number of rows
                if len(row) != len(grid[0]):
                    print('Invalid File Format: unequal number of characters per line')
                    del grid    # Ensures Turtle doesn't render the maze if file is invalid
                    filepath = turtle.textinput('Invalid File Format. Check Terminal', 'Enter File Name Below:')
                    continue

                # check for invalid characters in file
                for char in range(len(row)):
                    if row[char] not in ['X', '.', 's', 'e']:
                        print("Invalid File Format: Maze has invalid characters")
                        del grid    # Ensures Turtle doesn't render the maze if file is invalid
                        filepath = turtle.textinput('Invalid File Format. Check Terminal', 'Enter File Name Below:')
                        continue

                # check if vertical borders are all "X"
                if row[0] != "X" or row[-1] != "X":
                    print("Invalid File Format: Maze has incomplete borders")
                    del grid    # Ensures Turtle doesn't render the maze if file is invalid
                    filepath = turtle.textinput('Invalid File Format. Check Terminal', 'Enter File Name Below:')
                    continue

            # check if horizontal borders are all "X"
            if set(grid[0]) != {"X"} or set(grid[-1]) != {"X"}:
                print("Invalid File Format: Maze has incomplete borders")
                del grid    # Ensures Turtle doesn't render the maze if file is invalid
                filepath = turtle.textinput('Invalid File Format. Check Terminal', 'Enter File Name Below:')
                continue
            break
            

        print('File Validation Passed')
        turtle.clear()
        turtle.write('PIZZA RUNNERS: Done by Wee Leong & Ryan DAAA/FT/2B/05', font=("Verdana", 10, "normal"))
        turtle.ht()
        self.maze.setupmaze(grid)

aaa = FileIO()
aaa.validation()