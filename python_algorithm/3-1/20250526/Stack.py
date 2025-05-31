class Stack:
    def __init__(self, max = 5):
        self.MAX = max
        self.stack = [None] * self.MAX
        self.sp = 0
        pass

    def push(self, d):
        if self.sp < self.MAX:
            self.stack[self.sp] = d
            self.sp = self.sp + 1
            print("データ " + str(d) + " を追加しました")
        else:
            print("これ以上データを入れられません")

    def pop(self):
        if self.sp > 0:
            self.sp = self.sp - 1
            ret = self.stack[self.sp]
            self.stack[self.sp] = None
            return ret
        else:
            print("取り出すデータがありません")
            return None
        
    



