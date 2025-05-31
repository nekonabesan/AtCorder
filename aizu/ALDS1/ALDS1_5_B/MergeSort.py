class MergeSort:
    def __init__(self):
        self.cnt = 0
        self.MAX = 500000
        self.SENTINEL = 2000000000
        self.L = [None] * (self.MAX // 2 + 2)
        self.R = [None] * (self.MAX // 2 + 2)
        pass

    def merge(self, A, n, left, mid, right):
        n1 = mid - left
        n2 = right - mid
        for i in range(n1): self.L[i] = A[left + i]
        for i in range(n2): self.R[i] = A[mid + i]
        self.L[n1] = self.R[n2] = self.SENTINEL
        i = 0
        j = 0
        for k in range(left, right):
            self.cnt += 1
            if self.L[i] <= self.R[j]:
                A[k] = self.L[i]
                i += 1
            else:
                A[k] = self.R[j]
                j += 1

    def merge_sort(self, A, n, left, right):
        if (left + 1 < right):
            mid = (left + right) // 2
            self.merge_sort(A, n, left, mid)
            self.merge_sort(A, n, mid, right)
            self.merge(A, n, left, mid, right)
        return self.cnt, A


    