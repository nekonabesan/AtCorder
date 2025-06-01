############################################
# 3-5-2 隣接行列を用いた有向グラフの表現
############################################
class DirectedGraph:
    def __init__(self):
        self.data = [
            # 隣接行列
            [0, 1, 1, 0, 0]
            ,[0, 0, 1, 1, 0]
            ,[0, 0, 0, 0, 0]
            ,[0, 0, 0, 0, 1]
            ,[0, 0, 1, 1, 0]
        ]
        self.node = ['(0)', '(1)', '(2)', '(3)', '(4)']
        self.arrow = ['', '-->', '<--', '<->']
        pass

    def walk(self):
        for y in range(len(self.data)):
            for x in range(y, len(self.data[y])):
                pYtoX = self.data[y][x]
                pXtoY = self.data[x][y]
                a = pYtoX + pXtoY * 2
                if a > 0:
                    print(f"{self.node[y]} {self.arrow[a]} {self.node[x]}")
                

    
    