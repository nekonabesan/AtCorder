class QuickSort:
    def __init__(self, data = []):
        self.data = data
        pass

    def sort(self, left, right):
        i = left
        j = right
        pivot = self.data[(left + right) // 2]
        while True:
            while self.data[i] < pivot:
                i = i + 1
            while self.data[j] > pivot:
                j = j - 1
            if i >= j:
                break
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i = i + 1
            j = j - 1
        if left < i - 1:
            self.sort(left, i - 1)
        if j + 1 < right:
            self.sort(j + 1, right)
        
    
