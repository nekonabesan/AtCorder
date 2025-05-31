class Queue():
    def __init__(self, max = 6):
        self.MAX = max
        self.que = [None] * self.MAX
        self.head = 0
        self.tail = 0

    def enqueue(self, d):
        nt = (self.tail + 1) % self.MAX
        if nt == self.head:
            print("これ以上データを入れられません")
        else:
            self.que[self.tail] = d
            self.tail = nt
            print("データ " + str(d) + " を追加しました")

    def dequeue(self):
        d = None
        if self.head == self.tail:
            print("取り出すデータがありません")
        else:
            d = self.que[self.head]
            self.que[self.head] = None
            self.head = (self.head + 1) % self.MAX
        return d

