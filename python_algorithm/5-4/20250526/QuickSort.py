import random

class QuickSort:
    def __init__(self, n = 0, data = None):
        self.data = []
        if data is None:
            for _ in range(n):
                self.data = random.randint(1, 99)
        else:
            self.data = data
        self.n = len(self.data)
        pass

    def quick_sort(self, left, right):
        i = left
        j = right
        p = self.data[(left + right) // 2]
        while True:
            while self.data[i] < p:
                i += 1
            while self.data[j] > p:
                j -= 1
            if i >= j:
                break
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i += 1
            j -= 1
        if left < i - 1:
            self.quick_sort(left, i - 1)
        if right > j + 1:
            self.quick_sort(j + 1, right)
        
    def sort(self, data=None):
        if data is not None:
            self.data = data
            self.n = len(self.data)
        if len(self.data) == 0:
            return []
        print("Before sorting:", self.data)
        self.quick_sort(0, self.n - 1)
        print("After sorting:", self.data)
        return self.data
        