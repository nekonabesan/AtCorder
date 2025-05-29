class BinarySearch:
    def __init__(self):
        self.data = [1, 2 ,9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
        self.left = 0
        self.right = len(self.data) - 1
        self.flg = False
    
    def search(self, key = 0):
        while self.left <= self.right:
            mid = (self.left + self.right) // 2
            print("L={}, M={}, R={}".format(self.left, mid, self.right))
            if self.data[mid] == key:
                print("data[{}]が{}です".format(mid, key))
                self.flg = True
                break
            else:
                if self.data[mid] < key:
                    self.left = mid + 1
                else:
                    self.right = mid - 1
        if self.flg == False:
            print("データが見つかりませんでした")
        return self.flg


