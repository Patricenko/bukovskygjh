#binarny strom len s ukazovatelmi an ceu abecedu a dalej
class WordDictionary:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.child = {chr(i): None for i in range(ord('a'), ord('z') + 1)}

    def __init__(self):
        self.begin = self.Node()

    def insert(self,word,value):
        v = self.begin
        for c in word:
            if v.child[c] == None:
                v.child[c] = self.Node()
            v = v.child[c]
        v.value = value

    def walk(self, v, prefix=''):
        if v.value is not None:
            print(prefix + ' - ' + v.value)
        for c, child in v.child.items():
            if child is not None:
                self.walk(child, prefix + c)

    def load(self, filename="dict.txt"):
        with open(filename, "r") as f:
            for line in f:
                word, value = line.split(":")
                self.insert(word, value.strip())

    def save(self, filename="dict.txt"):
        with open(filename, "w") as f:
            def step(word, v):
                if v.value is not None:
                    f.write(word + ': ' + v.value + '\n')
                for p in v.child:
                    if v.child[p] is not None:
                        step(word + p, v.child[p])
            step('', self.begin)

    def find(self, prefix):
        v = self.begin
        for c in prefix:
            if v.child[c] is None:
                return f"'{prefix}' not found or has no continuations."
            v = v.child[c]
        matches = []
        def search(node, word):
            if node.value is not None:
                matches.append(f"{word}:{node.value}")
            for c, child in node.child.items():
                if child is not None:
                    search(child, word + c)
        search(v, prefix)
        if matches:
            return '\n'.join(matches)
        else:
            return f"No words found starting with '{prefix}'."
# Usage
s = WordDictionary()
s.load()
s.insert("keketenko","mongol")
s.insert("zambezia","zoltan")
print(s.find("keke"))
s.save()