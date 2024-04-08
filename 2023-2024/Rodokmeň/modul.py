import tkinter
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, levels):
        self.root = None
        self.levels = levels
        if levels > 0:
            self.root = self._create_complete_tree(levels)
    def _create_complete_tree(self, levels, current_level=0):
        if current_level >= levels:
            return None
        root = Node()
        root.left = self._create_complete_tree(levels, current_level + 1)
        root.right = self._create_complete_tree(levels, current_level + 1)
        return root

    def update_value(self, path, value):
        moves = [int(digit) for digit in str(path)]
        return self._update_value_by_path_recursive(self.root, moves, value)

    def _update_value_by_path_recursive(self, node, moves, value):
        if node is None or not moves:
            node.value = value
            return True
        if len(moves) == 1:
            if moves[0] == 2:
                if node.left is not None:
                    node.left.value = value
                    return True
                else:
                    node.left = Node(value)
                    return True
            elif moves[0] == 1:
                if node.right is not None:
                    node.right.value = value
                    return True
                else:
                    node.right = Node(value)
                    return True
            return False

        if moves[0] == 2:
            return self._update_value_by_path_recursive(node.left, moves[1:], value)
        elif moves[0] == 1:
            return self._update_value_by_path_recursive(node.right, moves[1:], value)
        else:
            return False
    def print_tree(self, node=None, level=0):
        if level == 0: print("##########################################################################")
        if level > self.levels: return
        if node is None:
            node = self.root
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

    def print_tree2(self):
        print("##########################################################################")
        levels = []
        self._collect_levels(self.root, 0, levels)
        for level in levels:
            print(" ".join(level))
        print("##########################################################################")

    def _collect_levels(self, node, depth, levels):
        if node is None:
            return
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(str(node.value))
        self._collect_levels(node.left, depth + 1, levels)
        self._collect_levels(node.right, depth + 1, levels)

class TButton:
    def __init__(self, win, text, x, y, level=0, bt=None, pos=""):
        self.win = win
        self.root = 0
        self.text = text
        self.x = x
        self.y = y
        self.level = level
        self.bt = bt
        self.pos = pos
        self.button = tkinter.Button(self.win, text=self.text, command=self.onClick, width=4, height=1)
        self.button.place(x=self.x, y=self.y)
    def updateme(self, text):
        self.text = text
        self.button.config(text=self.text)
        self.bt.update_value(path=self.pos, value=self.text)
        self.bt.print_tree()
        self.bt.print_tree2()
    def onClick(self):
        create_input_window(prompt="Enter your desired change:", callback=self.updateme)

def create_input_window(prompt, callback):
    def on_submit():
        user_input = input_field.get()
        callback(user_input)
        window.destroy()
    window = tkinter.Toplevel()
    window.title(prompt)
    tkinter.Label(window, text=prompt).pack(side="top", fill="x", pady=10)
    input_field = tkinter.Entry(window)
    input_field.pack(side="top", fill="x", padx=10)
    input_field.focus_set()
    submit_button = tkinter.Button(window, text="Submit", command=on_submit)
    submit_button.pack(side="bottom", fill="x", padx=10, pady=10)
