class TreeSearch():
    def __init__(self):
        self.LEFT = 0
        self.RIGHT = 1
        self.DATA = 2
        self.node = [
            [1, 2, 10]
            ,[3, 4, 5]
            ,[5, None, 12]
            ,[None, None, 2]
            ,[6, 7, 8]
            ,[None, None, 11]
            ,[None, None, 6]
            ,[None, None, 9]
        ]
    
    def traverse(self, p):
        if p != None:
            self.traverse(self.node[p][self.LEFT])
            print(self.node[p][self.DATA])
            self.traverse(self.node[p][self.RIGHT])
            
    