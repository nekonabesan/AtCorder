class ShellSort:
    def __init__(self, A = [], n =0):
        self.A = A
        self.n = n
        self.G = []
        self.cnt = 0
        pass

    def insert_sort(self, A = [], n = 0, g = 0):
        for i in range(g, n):
            v = A[i]
            j = i - g
            while j >= 0 and A[j] > v:
                A[j + g] = A[j]
                j -= g
                self.cnt += 1
            A[j + g] = v
        return A
    
    def shell_sort(self, A = [], n = 0):
        G = []
        h = 1
        while h < n:
            G.append(h)
            h = 3 * h + 1
        G.reverse()
        self.G = G
        for i in range(0, len(self.G)):
            g = self.G[len(self.G) - 1 - i]
            A = self.insert_sort(A, n, g)
            
        return A

    def sort(self, A = [], n =0):
        if A != []: self.A = A
        if n != 0: self.n = n
        A = self.shell_sort(self.A, self.n)

        print(len(self.G))
        for i in range(0, len(self.G)):
            if i == len(self.G) - 1:
                print(self.G[i])
            else:
                print(self.G[i], end=' ')
    
        print(self.cnt)
        for i in range(0, len(A)):
            print(A[i])
        return self.cnt, A