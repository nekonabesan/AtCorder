class DataStructure:
    def __init__(self, index = None, value = None, prev = None, next = None):
        self.index = index
        self.value = value
        self.prev = prev
        self.next = next

class LinearBinarySearch:
    def __init__(self):
        self.index = None
        self.right = None
        self.mid = None
        self.hp = None
        self.tp = None
        self.length = None

    def init_data(self, data = []):
        if len(data) == 0:
            return None
        prev = None
        for i in range(0, len(data)):
            node = DataStructure(i, data[i], prev, None)
            if i == 0:
                self.hp = node
            else:
                prev.next = node
                self.tp = node
            self.length = i + 1
            prev = node
        return node
    
    def head(self):
        if self.hp is None:
            return None
        node = self.hp
        while node.prev is not None:
            node = node.prev
        return node
    
    def tail(self):
        if self.tp is None:
            return None
        node = self.tp
        while node.next is not None:
            node = node.next
        return node

    def get_node_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head()
        while node.index != index:
            node = node.next
        return node
    
    def search(self, left = 0, right = 0, key = 0):
        flg = False
        ret = None
        # left <= rightの間繰り返す
        while left <= right:
            # midをleftとrightの中間の値に設定
            mid = int((left + right) // 2)
            node = self.get_node_by_index(mid)
            if node is None:
                break
            if node.value == key:
                flg = True
                ret = node
                break
            if node.value < key:
                # midの値をleftに設定
                left = mid + 1
            else:
                # midの値をrightに設定
                right = mid - 1
            if left > right:
                ret = None
                break
        return ret

    
    