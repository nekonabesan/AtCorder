from Tree import Tree

if __name__ == '__main__':
    tree = Tree()
    root = tree.root
    root.value = 10
    tree.add_child(root, 20, 30)
    parent = tree.find(20)
    tree.add_child(parent, 40, 50)
    pass
