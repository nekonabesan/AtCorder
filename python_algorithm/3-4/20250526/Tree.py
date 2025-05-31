class Tree:
    def __init__(self):
        self.LEFT = 0
        self.RIGHT = 1
        self.DATA = 2
        self.node = [
            [1, 2, 10]
            ,[3, 4, 20]
            ,[5, None, 30]
            ,[None, None, 40]
            ,[6, 7, 50]
            ,[None, None, 60]
            ,[None, None, 70]
            ,[None, None, 80]
        ]
        self.MAX = len(self.node)

    def walk(self, s = 0):
        ret = None
        left = None
        right = None

        n = int(s)
        if 0 <= n and n < self.MAX:
            print("node{}の値は{}".format(n, self.node[n][self.DATA]))
            ret = self.node[n][self.DATA]
            if self.node[n][self.LEFT] != None:
                left = self.node[n][self.LEFT]
                print("左の子は{}".format(n, left))
            else:
                print("左の子は存在しない")
            if self.node[n][self.RIGHT] != None:
                right = self.node[n][self.RIGHT]
                print("右の子は{}".format(n, right))
            else:
                print("右の子は存在しない")
        else:
            print("0から" + str(self.MAX) + "の範囲で入力してください")
        return ret, left, right



    