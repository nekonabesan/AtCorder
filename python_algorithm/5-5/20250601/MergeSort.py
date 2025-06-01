class MergeSort:
    def __init__(self, data = []):
        self.data = data
    
    def merge(self, left, mid, right):
        buff = [None] * (right - left)
        i = left
        j = mid
        p = 0
        while i < mid and j < right:
            if self.data[i] <= self.data[j]:
                buff[p] = self.data[i]
                i += 1
                p += 1
            else:
                buff[p] = self.data[j]
                j += 1
                p += 1
        while i < mid:
            buff[p] = self.data[i]
            i += 1
            p += 1
        while j < right:
            buff[p] = self.data[j]
            j += 1
            p += 1
        for n in range(left, right):
            self.data[n] = buff[n - left]

    def sort(self):
        s = 2
        n = len(self.data)
        while s <= n:
            loop = n//s
            fragment = n % s
            for i in range(loop):
                self.merge(i * s, i * s + (s//2), i * s + s)
            if fragment > 0:
                self.merge((loop - 1) * s, loop * s, n)
            s *= 2
        return self.data
    