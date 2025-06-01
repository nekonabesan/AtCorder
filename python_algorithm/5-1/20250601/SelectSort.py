class SelectSort:
    def __init__(self):
        pass

    def sort(self, data = []):
        n = len(data)
        for i in range(n):
            for j in range(i + 1, n):
                if data[j] < data[i]:
                    data[i], data[j] = data[j], data[i]
        return data