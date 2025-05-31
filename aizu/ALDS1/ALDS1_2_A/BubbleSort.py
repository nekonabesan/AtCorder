class BubbleSort:
    def __init__(self, A = [], N = 0):
        self.A = A
        self.N = N
        pass

    def sort(self, A = [], N = 0):
        if A != None:
            self.A = A
        if N != 0:
            self.N = N
        if A == []:
            return A
        flg = True
        c = 0
        while flg:
            flg = False
            for j in range(1, self.N):
                if self.A[j] < self.A[j - 1]:
                    self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
                    flg = True
                    c += 1
        for j in range(self.N):
            if j == self.N - 1:
                print(self.A[j])
            else:
                print(self.A[j], end=' ')
        print(c)
        return c, A