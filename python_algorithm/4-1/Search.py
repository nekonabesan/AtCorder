class Search:
    def __init__(self):
        self.data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]

    def execute(self, k = 0):
        n = len(self.data)
        key = k
        flg = False
        for i in range(n):
            if self.data[i] == key:
                flg = True
                break
        if flg == False:
            print("Element not found")
        return flg