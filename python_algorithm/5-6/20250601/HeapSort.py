class HeapSort:
    def __init__(self):
        pass

    def sort(self, data):
        n = len(data)
        for  i in range((n - 1)//2, -1, -1):
            p = i
            c = p * 2 + 1
            while c < n:
                if c < n - 1 and data[c] < data[c + 1]:
                    c += 1
                if data[p] >= data[c]:
                    break
                data[p], data[c] = data[c], data[p]
                p = c
                c = p * 2 + 1
        d = n - 1
        while d > 0:
            data[0], data[d] = data[d], data[0]
            p = 0
            c = p * 2 + 1
            while c < d:
                if c < d - 1 and data[c] < data[c + 1]:
                    c += 1
                if data[p] >= data[c]:
                    break
                data[p], data[c] = data[c], data[p]
                p = c
                c = p * 2 + 1
            d -= 1
        return data

