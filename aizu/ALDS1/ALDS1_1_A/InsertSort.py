class InsertSort:
    def __init__(self):
        pass

    def trace(self, A = []):
        for i in range(len(A)):
            if i > 0:
                print(" ", end='')
            print(A[i], end='')
        print("")

    def sort(self, A = [], N = 0):
        i = None
        j = None
        v = None
        for i in range(1, N):
            v = A[i]
            j = i - 1
            while j >= 0 and A[j] > v:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = v
            self.trace(A)
        return A