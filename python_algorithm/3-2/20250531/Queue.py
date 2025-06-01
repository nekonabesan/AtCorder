class DataStructure:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        pass

class Queue:
    def __init__(self):
        ds = DataStructure()
        self.hp = ds
        self.tp= ds
        pass

    def is_empty(self):
        if self.hp == self.tp and self.hp.value is None:
            return True

    def enqueue(self, value):
        new_node = DataStructure(value)
        tail = self.tail()
        if tail is not None:
            tail.next = new_node
            new_node.prev = tail
            self.tp = new_node
        else: 
            self.hp = new_node
            self.tp = new_node
        return self.tp

    def dequeue(self):
        hd = self.head()
        value = hd.value
        self.hp = hd.next
        if self.hp is not None:
            self.hp.prev = None
        else:
            self.hp = None
            self.tp = None
            pass
        hd = None
        return value

    def size(self):
        hd = self.head()
        count = 0
        while hd is not None:
            count += 1
            hd = hd.next
        return count

    def head(self):
        hd = self.hp
        while hd is not None and hd.prev is not None:
            hd = hd.prev
        return hd
    
    def tail(self):
        tail = self.tp
        while tail is not None and tail.next is not None:
            tail = tail.next
        return tail