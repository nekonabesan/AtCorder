class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTreeSearch:
    def __init__(self):
        self.root = Node()
        self.ret = []
        pass

    def find(self, current, value):
        if current is None:
            return None
        if current.value == value:
            return current
        return self.find(current.left, value) or self.find(current.right, value)
        
    def insert(self, value, parent=None, pl=None, pr=None):
        if parent is None:
            self.root.value = value
            return self.root
        new_node = Node(value)
        new_node.parent = parent
        if pl is not None:
            parent.left = new_node
        elif pr is not None:
            parent.right = new_node
        return new_node
    
    def tarverse(self, current):
        # 二分探索木を通りがけ順に巡回
        if current is None:
            return None
        self.tarverse(current.left)
        self.ret.append(current.value)
        print(current.value)
        self.tarverse(current.right)


        

        

    

    
    


    