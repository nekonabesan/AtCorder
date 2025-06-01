import math

class Prime:
    def __init__(self, max = 100):
        self.max = max
        self.map = [True] * (self.max + 1)
        self.map[0] = False
        self.map[1] = False
        pass

    def is_prime(self):
        ret = []
        limit = int(math.sqrt(self.max)) + 1
        for i in range(2, limit):
            if self.map[i] == True:
                j = 1
                h = i * j
                while h < self.max + 1:
                    if h == i:
                        pass
                    elif h % i == 0:
                        self.map[h] = False
                        pass
                    j += 1
                    h = i * j
            else:
                continue
        for i in range(2, self.max + 1):
            if self.map[i] == True:
                ret.append(i)
        #print(self.p)
        return ret

    