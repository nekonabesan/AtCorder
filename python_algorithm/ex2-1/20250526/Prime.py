class Prime:
    def __init__(self, n = 2, p = [True] * 100):
        self.n = n
        self.p = p
        self.P = []


    def hyou(self):
        self.s = ""
        for i in range(100):
            if self.p[i] == True:
                self.s += "{:2d}, ".format(i)
                self.P.append(i)
            else:
                self.s += "/, "
            if i % 10 == 9:
                self.s += "\n"
            #print(self.s)

    def furui(self):
        for i in range(self.n + self.n, 100, self.n):
            self.p[i] = False
        print(self.n, "の倍数をふるい落とし")
        #self.hyou()
        while self.n < 100:
            self.n = self.n + 1
            if self.p[self.n] == True:
                break

    def prime(self):
        self.p[0] = False
        self.p[1] = False
        #self.hyou()
        while self.n < 10:
            self.furui()
        self.hyou()
        print("素数は", self.P)
    
