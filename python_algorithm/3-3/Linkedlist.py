class LinkedList:
    def __init__(self, max = 5):
        self.MAX = 5
        self.data = [None] * self.MAX
        self.pointer = [None] * self.MAX
        self.head = 0
        pass

    def add_list(self, d):
        n = -1
        for i in range(self.MAX):
            if self.data[i] == None:
                n = i
                break
        if n == -1:
            print("List is full")
            return False
        for i in range(self.MAX):
            if self.data[i] != None and self.pointer[i] == None:
                self.pointer[i] = n
                break
        
        self.data[n] = d
        self.pointer[n] = None

        print("データ " + str(d) + " を追加しました")
        return True
    
    def del_list(self, d):
        n = -1
        for i in range(self.MAX):
            if self.data[i] == d:
                n = i
                break
        if n == -1:
            print("データは存在しません")
            return False
        if n != self.head:
            for i in range(self.MAX):
                if self.pointer[i] == n:
                    self.pointer[i] = self.pointer[n]
        else:
            self.head = self.pointer[n]
            if self.head == None:
                self.head = 0
        self.data[n] = None
        self.pointer[n] = None
        print("データ " + str(d) + " を削除しました")
        return True
    
    def put_list(self):
        p = self.head
        while True:
            print(self.data[p], end=" -> ")
            if self.pointer[p] is None:
                print("EOF")
                break
            p = self.pointer[p]

        


        


            