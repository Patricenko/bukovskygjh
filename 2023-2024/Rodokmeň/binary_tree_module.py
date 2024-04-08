# binary_tree_module.py

class Node:
    def __init__(self, name="0", level=0):
        self.name = name
        self.level = level
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, levels):
        self.levels = levels
        self.root = None
        self.create_tree()

    def create_tree(self):
        self.root = Node(level=1)
        current_nodes = [self.root]
        level = 1
        while level < self.levels:
            next_nodes = []
            for n in current_nodes:
                n.left = Node(level=level + 1)
                n.right = Node(level=level + 1)
                next_nodes.extend([n.left, n.right])
            level += 1
            current_nodes = next_nodes

    def get_nodes_by_level(self, level):
        if level == 0:
            return [self.root]
        result = []
        nodes = [self.root]
        while nodes and level > 0:
            next_nodes = []
            for node in nodes:
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
            level -= 1
            nodes = next_nodes
        return nodes

    def get_total_levels(self):
        current = self.root
        total_levels = 0
        while current:
            total_levels += 1
            current = current.left  # Assuming a perfect binary tree
        return total_levels
