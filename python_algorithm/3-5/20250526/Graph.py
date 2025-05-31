class Graph:
    def __init__(self):
        self.data = [
            [0, 1, 1, 0, 0]
            ,[0, 0, 1, 1, 0]
            ,[0, 0, 0, 0, 0]
            ,[0, 0, 0, 0, 1]
            ,[0, 0, 1, 1, 0]
        ]
        self.node = ["(0)", "(1)", "(2)", "(3)", "(4)"]
        self.arrow = ["", "-->", "<--", "<-->"]

    
    def walk(self):
        ret = []
        for y in range(len(self.data)):
            for x in range(y, len(self.data[y])):
                e1 = self.data[y][x]
                e2 = self.data[x][y]
                a = e1 + e2 * 2
                if a > 0:
                    ret.append(f"{self.node[y]} {self.arrow[a]} {self.node[x]}")
                    print(f"{self.node[y]} {self.arrow[a]} {self.node[x]}")
        return ret

