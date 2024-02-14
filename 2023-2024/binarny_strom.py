import front_stack as fs
#navrh struktury

class Item:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, info):
        self.root = Item(info) #self.begin fancyyyyy
        self.size = 0
        self.items = []
        self.stack = []
    def printTree(self, item=None, l=[]):
        if item is None: item = self.root; l.append(item.info)
        if item.right is not None:
            l.append(item.right.info)
            self.printTree(item.right, l)
        if item.left is not None:
            l.append(item.left.info)
            self.printTree(item.left, l)
        else: return
        return l


tree= BinaryTree(10)
tree.root.right = Item(5)
tree.root.right.right = Item(6)
tree.root.right.left = Item(7)
tree.root.left = Item(8)
tree.root.left.right = Item(9)
print(tree.printTree())

