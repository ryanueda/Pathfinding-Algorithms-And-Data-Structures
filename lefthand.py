import networkx as nx

class LeftHand():
    # TO-DO: EDIT IF CONDITION
    def __init__(self, start, finish, walls, boxes):
        self.start = start
        self.finish = finish
        self.walls = walls
        self.boxes = boxes
        self.G = nx.Graph()

    def working(self):
        self.G.add_nodes_from(self.walls)
        self.G.add_nodes_from(self.boxes)
        self.G.add_nodes_from(self.start)
        self.G.add_nodes_from(self.finish)

        for i in range(len(self.walls)):
            for j in range(len(self.walls)):
                if i != j:
                    if (self.walls[i][0] - self.walls[j][0] == 24) or (self.walls[i][1] - self.walls[j][1] == 24):
                    # if abs(self.walls[i][0] - self.walls[j][0]) + abs(self.walls[i][1] - self.walls[j][1]) == 1:
                        self.G.add_edge(self.walls[i], self.walls[j])

        for i in range(len(self.boxes)):
            for j in range(len(self.boxes)):
                if i != j:
                    if (self.boxes[i][0] - self.boxes[j][0] == 24) or (self.boxes[i][1] - self.boxes[j][1] == 24):
                    # if abs(self.boxes[i][0] - self.boxes[j][0]) + abs(self.boxes[i][1] - self.boxes[j][1]) == 1:
                        self.G.add_edge(self.boxes[i], self.boxes[j])

        # for i in range(len(self.walls)):
        #     for j in range(len(self.boxes)):
        #         if abs(self.walls[i][0] - self.boxes[j][0]) + abs(self.walls[i][1] - self.boxes[j][1]) == 1:
        #             self.G.add_edge(self.walls[i], self.boxes[j])

        for i in range(len(self.start)):
            for j in range(len(self.boxes)):
                if (abs(self.start[i][0] - self.boxes[j][0]) == 24) or (abs(self.start[i][1] - self.boxes[j][1]) == 24):
                # if abs(self.start[i][0] - self.boxes[j][0]) + abs(self.start[i][1] - self.boxes[j][1]) == 1:
                    self.G.add_edge(self.start[i], self.boxes[j])

        for i in range(len(self.finish)):
            for j in range(len(self.boxes)):
                if (abs(self.finish[i][0] - self.boxes[j][0]) == 24) or (abs(self.finish[i][1] - self.boxes[j][1]) == 24):
                # if abs(self.finish[i][0] - self.boxes[j][0]) + abs(self.finish[i][1] - self.boxes[j][1]) == 1:
                    self.G.add_edge(self.finish[i], self.boxes[j])

        # print(self.G.edges)
        self.path = nx.shortest_path(self.G, self.start[0], self.finish[0])
        print(self.path)
