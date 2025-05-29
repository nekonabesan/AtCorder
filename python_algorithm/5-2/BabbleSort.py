class BabbleSort:
    def __init__(self, data = [9,4,7,2,3,8,6,1,5,0]):
        self.data = data

    def sort(self):
        print(self.data, "Babble Sort")
        n = len(self.data)
        for i in range(0, n - 1):
            for j in range(n - 1, i, - 1):
                if self.data[j - 1] > self.data[j]:
                    self.data[j], self.data[j - 1] = self.data[j - 1], self.data[j]
        print(self.data, "Sorted")
        return self.data