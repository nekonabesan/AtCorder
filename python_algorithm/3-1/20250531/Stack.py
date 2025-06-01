class DataStructure:
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        pass

class Stack:
    def __init__(self):
        self.sp = DataStructure()
        self.sp.value = None
        self.sp.prev = None
        self.sp.next = None
        pass

    def push(self, value):
        head = self.sp
        while self.sp.prev is not None:
            head = self.sp.prev
        if head.value == None:
            head.value = value
            self.sp = head
        else:
            next = self.sp
            self.sp = DataStructure(value, None, next)
            next.prev = self.sp
        pass

    def pop(self):
        head = self.sp
        while self.sp.prev is not None:
            head = self.sp.prev
        if head is None:
            self.sp = DataStructure()
            value = self.sp.value
        else:
            value = head.value
            if head.next is not None:
                self.sp = head.next
                self.sp.prev = None
            else:
                self.sp = DataStructure()
                self.sp.value = None

        return value


        