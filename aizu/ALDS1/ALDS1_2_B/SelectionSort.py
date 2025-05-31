class SelectionSort:
    def __init__(self, A = [], N = 0):
        self.A = A
        self.N = N
        pass
    
    def trace(self, A = []):
        for i in range(len(A)):
            if i > 0:
                print(" ", end='')
            print(A[i], end='')
        print("")

    def sort(self, A = [], N = 0):
        if self.A != None:
            self.A = A
        if N != 0:
            self.N = N
        c = 0
        for i in range(self.N):
            minj = i
            for j in range(i, self.N):
                if self.A[j] < self.A[minj]:
                    minj = j
            self.A[i], self.A[minj] = self.A[minj], self.A[i]
            if i != minj: c += 1
        self.trace(self.A)
        print(c)

        return c, self.A
    