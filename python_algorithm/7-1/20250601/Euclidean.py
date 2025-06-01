class Euclidean:
    def __init__(self):
        pass

    def euclid(self, a, b):
        ret = None
        while True:
            r = a % b
            if r == 0:
                ret = b
                break
            a, b = b, r
        return ret