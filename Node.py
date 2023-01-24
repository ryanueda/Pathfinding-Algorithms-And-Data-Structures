class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # G Cost - Distance from starting node
        self.g = 0

        # H Cost - Distance from end node
        self.h = 0

        # F Cost - G Cost + H Cost
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position