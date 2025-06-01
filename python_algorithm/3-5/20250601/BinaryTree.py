############################################
# 3-5-1 隣接行列を用いた二分木の表現
############################################
class BinaryTree:
    def __init__(self):
        self.data = [
            # 隣接行列
            [0, 1, 1, 0, 0]
            ,[1, 0, 0, 1, 1]
            ,[1, 0, 0, 0, 0]
            ,[0, 1, 0, 0, 0]
            ,[0, 1, 0, 0, 0]
        ]
        self.node = ['(0)', '(1)', '(2)', '(3)', '(4)']
        pass

    def walk(self):
        for y in range(len(self.data)):
            for x in range(y, len(self.data[y])):
                if self.data[y][x] == 1 and self.data[x][y] == 1:
                    print(f"{self.node[y]} <-> {self.node[x]}")
        
        

    