import math

class Prime:
    def __init__(self, max = 100):
        self.max = max
        self.p = [False] * max
        self.p[0] = self.p[1] = False
        self.n = 2
        pass

    def is_prime(self):
        for i in range(self.n, self.max):
            if i > math.sqrt(self.max):
                break
            self.p[i] = False
            if self.p[i] == True:
                continue
            for j in range(i, self.max, j * i):
                if i % j == 0:
                    self.p[j] = True
        return self.p



                

    