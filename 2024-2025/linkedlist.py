class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    def __init__(self):
        self.begin = None
        self.last = None
    def append(self, value):
        if self.begin == None:
            self.begin = self.Node(value)
            self.last = self.begin
        else:
            self.last.next = self.Node(value)
            self.last = self.last.next

    def prepend(self, value):
        if self.begin == None:
            self.begin = self.Node(value)
            self.last = self.begin
        else:
            p = self.Node(value)
            p.next = self.begin
            self.begin = p

    def concat(self, other):
        self.last.next = other.begin
        self.last = other.last
        other = None
        
    def insert(self,pos,value):
        if self.begin == None:
            self.begin = self.Node(value)
        else:
            pp = LinkedList()
            p = self.begin
            i = 0
            while p != None:
                if pos == i:
                    pp.append(value)
                else:
                    pp.append(p.value)
                    p = p.next
                i += 1
            self.begin = pp.begin
    def printl(self):
        p = self.begin
        while p != None:
            print(p.value)
            p = p.next
    def reverse(self, value):
        novy = LinkedList()
        p = self.begin
        while p != None:
            novy.prepend(p.value)
            p = p.next
    def len(self):
        i = 0
        p = self.begin
        while p != None:
            p = p.next
            i += 1
        return i
    def copy(self):
        cc = LinkedList()
        p = self.begin
        while p != None:
            cc.append(p.value)
            p = p.next
        return cc

    def pop(self):
        if self.begin == None:
            return None
        else:
            p = self.begin
            self.begin = p.next
            return p.value




