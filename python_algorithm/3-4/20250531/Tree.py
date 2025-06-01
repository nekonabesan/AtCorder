class Node:
    def __init__(self, value = None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        pass

class Tree:
    def __init__(self, value = None):
        self.root = Node(value)

    def find(self, value, node=None):
        if node is None:
            return None
        if node.value == value:
            return node
        return self.find(value, node.left) or self.find(value, node.right)
        
    def add_child(self, parent, lv=None, rv=None):
        left = right = None
        if lv is not None:
            left = Node(lv, parent)
        if rv is not None:
            right = Node(rv, parent)
        parent.left = left
        parent.right = right
        return parent

    
