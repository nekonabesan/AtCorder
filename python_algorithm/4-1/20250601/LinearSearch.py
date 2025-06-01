################################################
# 4-1 Linear Search
################################################
class DataStructure:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class LinearSearch:
    def __init__(self, data = None, key = None):
        self.data = data
        self.key = key
        self.flg = False
        self.hd = None
        self.td = None

    def init_data(self, data = None):
        if data is not None:
            self.data = data
        prev = None
        for i in range(len(self.data)):
            node = DataStructure(self.data[i])
            if i == 0:
                self.hd = node
            node.prev = prev
            if prev is not None:
                prev.next = node
            node.next = None
            prev = node
        self.td = node
    
    def head(self):
        if self.hd is None:
            return None
        p = self.hd
        while p.prev is not None:
            p = p.prev
        return p
    
    def tail(self):
        if self.td is None:
            return None
        p = self.td
        while p.next is not None:
            p = p.next
        return p

    def search(self, key = None):
        if self.hd is None:
            return None
        p = self.head()
        ret = None
        while p.next is not None:
            if p.value == key:
                ret = p
                break
            p = p.next
        return ret