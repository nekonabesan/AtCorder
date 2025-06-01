class BabbleSort:
    def __init__(self):
        pass

    def sort(self, data = []):
        for i in range(len(data) - 1):
            j = len(data) - 1
            while j > i:
                if data[j] < data[j - 1]:
                    data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
        return data
    