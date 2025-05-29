class MergeSort:
    def __init__(self, a =[], b = []):
        self.a = a
        self.b = b
        self.init()
        pass

    def init(self):
        self.na = len(self.a)
        self.nb = len(self.b)
        self.c = [0] * (self.na + self.nb)
        self.i = 0
        self.j = 0
        self.p = 0
        return

    def merge_sort(self):
        while self.i < self.na and self.j < self.nb:
            if self.a[self.i] <= self.b[self.j]:
                self.c[self.p] = self.a[self.i]
                self.i += 1
            else:
                self.c[self.p] = self.b[self.j]
                self.j += 1
            self.p += 1

        while self.i < self.na:
            self.c[self.p] = self.a[self.i]
            self.i += 1
            self.p += 1

        while self.j < self.nb:
            self.c[self.p] = self.b[self.j]
            self.j += 1
            self.p += 1
        return
    
    def sort(self, a = None, b = None):
        if a != None:
            self.a = a
            self.na = len(self.a)
        if b != None:
            self.b = b
            self.nb = len(self.b)
        if self.na == 0 and self.nb == 0:
            print("Both arrays are empty, returning empty list.")
            return []
        self.init()
        print("Sorting arrays:", self.a, "and", self.b)
        self.merge_sort()
        print("Sorted array:", self.c)
        return self.c

