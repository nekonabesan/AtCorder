class InsertSort:
    def __init__(self, data = [9,2,4,7,8,3,1,5,6,0]):
        self.data = data
        pass

    def sort(self):
        print("Before sort:", self.data)
        n = len(self.data)
        for i in range(1, n):
            tmp = self.data[i]
            j = i
            while j > 0 and self.data[j - 1] > tmp:
                self.data[j] = self.data[j - 1]
                j = j - 1
            self.data[j] = tmp
        print("After sort:", self.data)
        return self.data
