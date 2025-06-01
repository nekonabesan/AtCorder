class Dijkstra:
    def __init__(self):
        self.F = 99999
        self.way = [
            [self.F, 3, 2, 5, self.F, self.F, self.F]
            ,[3, self.F, self.F, self.F, 7, self.F, self.F]
            ,[2, self.F, self.F, 2, self.F, 4, self.F]
            ,[5, self.F, 2, self.F, self.F, 1, self.F]
            ,[self.F, 7, self.F, self.F, self.F, 4, 5]
            ,[self.F, self.F, 4, 1, 4, self.F, 3]
            ,[self.F, self.F, self.F, self.F, 5, 3, self.F]
        ]
        self.dist = [self.F] * 7
        self.flg = [0] * 7
        self.route = [-1] * 7

    def dijkstra(self):
        start = 0
        p = start
        self.dist[p] = start
        for i in range(7):
            d = self.F
            for j in range(7):
                if self.flg[j] == 0 and self.dist[j] < d:
                    p = j
                    d = self.dist[j]
            self.flg[p] = 1
            for k in range(7):
                if self.dist[p] + self.way[p][k] < self.dist[k]:
                    self.dist[k] = self.dist[p] + self.way[p][k]
                    self.route[k] = p

    def get_distances(self, s=0, e=0):
        d = []
        r = []
        for i in range(7):
            print("ノード{}まで {}".format(str(i), str(self.dist[i])))
            d.append(self.dist[i])
        print("routeの値: {}".format(self.route))
        while self.route[e] >= 0:
            print(e, end="<-")
            r.append(e)
            e = self.route[e]
        print(s)
        r.append(s)
        
        return d,r
        

            