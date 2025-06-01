class InsertSort:
    def __init__(self):
        pass
    
    def sort(self, data):
        for i in range(1, len(data)):
            tmp = data[i]
            j = i
            while j > 0 and data[j - 1] > tmp:
                data[j] = data[j - 1]
                j -= 1
            data[j] = tmp
        return data