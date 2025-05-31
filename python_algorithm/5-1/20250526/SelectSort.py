class SelectSort:
    def __init__(self, data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]):
        self.data = data
        pass

    def sort(self):
        print("Before sorting:", self.data)
        for i in range(len(self.data)):
            m = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[m]:
                    m = j
            self.data[i], self.data[m] = self.data[m], self.data[i]
        print("After sorting:", self.data)
        return self.data
