import tkinter
class Vertex:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, levels):
        self.root = None
        self.levels = levels
        if levels > 0:
            self.root = self.createTree(levels)
    def createTree(self, levels, current_level=0):
        if current_level >= levels:
            return None
        root = Vertex()
        root.left = self.createTree(levels, current_level + 1)
        root.right = self.createTree(levels, current_level + 1)
        return root

    def update_value(self, path, value):
        moves = [int(digit) for digit in str(path)]
        return self.rekurzia(self.root, moves, value)

    def rekurzia(self, vertex, moves, value):
        if vertex is None or not moves:
            vertex.value = value
            return True
        if len(moves) == 1:
            if moves[0] == 2:
                if vertex.left is not None:
                    vertex.left.value = value
                    return True
                else:
                    vertex.left = Vertex(value)
                    return True
            elif moves[0] == 1:
                if vertex.right is not None:
                    vertex.right.value = value
                    return True
                else:
                    vertex.right = Vertex(value)
                    return True
            return False

        if moves[0] == 2:
            return self.rekurzia(vertex.left, moves[1:], value)
        elif moves[0] == 1:
            return self.rekurzia(vertex.right, moves[1:], value)
        else:
            return False
    def print_tree(self, vertex=None, level=0):
        if level == 0: print("##########################################################################")
        if level > self.levels: return
        if vertex is None:
            vertex = self.root
        if vertex is not None:
            self.print_tree(vertex.right, level + 1)
            print(' ' * 4 * level + '->', vertex.value)
            self.print_tree(vertex.left, level + 1)

    def print_tree2(self):
        print("##########################################################################")
        levels = []
        self.rekurzia2(self.root, 0, levels)
        for level in levels:
            print(" ".join(level))
        print("##########################################################################")

    def rekurzia2(self, vertex, depth, levels):
        if vertex is None:
            return
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(str(vertex.value))
        self.rekurzia2(vertex.left, depth + 1, levels)
        self.rekurzia2(vertex.right, depth + 1, levels)

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
