from subprocess import call
class WordDictionary:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.child = {chr(i): None for i in range(ord('a'), ord('z') + 1)}

    def __init__(self):
        self.begin = self.Node()
        self.debug = False

    def insert(self,word,value,filename, first=False):
        active = False
        if self.find(word, filename): active = True
        v = self.begin
        for c in word:
            if v.child[c] == None:
                v.child[c] = self.Node()
            v = v.child[c]
        if active: v.value += ", " + value
        else: v.value = value
        if not first:
            self.save(filename)
            call("python converter.py")
        return f"Inserted {word}: {value} to {filename} successfully."
    def walk(self, v, prefix=''):
        if v.value is not None:
            print(prefix + ' - ' + v.value)
        for c, child in v.child.items():
            if child is not None:
                self.walk(child, prefix + c)

    def erase(self):
        self.begin = self.Node()
        return "Erased dictionary successfully."

    def load(self, filename, first=False):
        with open(filename, "r") as f:
            for line in f:
                if line == '\n': continue
                if line.split(":")[1] == "": word = line.split(":")[0]; value = ""
                else: word, value = line.split(":")
                self.insert(word.lower(), value.strip().lower(), filename, first)
        return f"Loaded {filename} successfully."

    def save(self, filename="dict.txt"):
        with open(filename, "w") as f:
            def step(word, v):
                if v.value is not None:
                    f.write(word + ': ' + v.value + '\n')
                for p in v.child:
                    if v.child[p] is not None:
                        step(word + p, v.child[p])
            step('', self.begin)
        return f"Saved {filename} successfully."

    def find(self, prefix, filename):
        v = self.begin
        for c in prefix.lower():
            if v.child[c] is None:
                return []
            v = v.child[c]
        matches = []
        def search(node, word):
            if node.value is not None:
                if filename == "subjectToName.txt": word = word.upper(); node.value = node.value.capitalize()
                else: word = word.capitalize(); node.value = node.value.upper()
                matches.append(f"{word}: {node.value}")
            for c, child in node.child.items():
                if child is not None:
                    search(child, word + c)
        search(v, prefix)
        if matches:
            return matches
        else:
            return []