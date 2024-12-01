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

    def __iter__(self):
        self.p = self.begin
        return self
    def __next__(self):
        if self.p != None:
            value = self.p.value
            self.p = self.p.next
            return value
        else:
            raise StopIteration
    def __getitem__(self, index):
        p = self.begin
        for i in range(index):
            if p == None:
                raise IndexError
            p = p.next
        if p == None:
            raise IndexError
        return p.value
    def __setitem__(self, index, value):
        p = self.begin
        for i in range(index):
            if p == None:
                raise IndexError
            p = p.next
        if p == None:
            raise IndexError
        p.value = value
    def __len__(self):
        i = 0
        p = self.begin
        while p != None:
            p = p.next
            i += 1
        return i
    def __add__(self, other):
        novy = LinkedList()
        p = self.begin
        while p != None:
            novy.append(p.value)
            p = p.next
        p = other.begin
        while p != None:
            novy.append(p.value)
            p = p.next
        return novy
    def __mul__(self, n):
        novy = LinkedList()
        for _ in range(n):
            p = self.begin
            while p != None:
                novy.append(p.value)
                p = p.next
        return novy
    def __eq__(self, other):
        p = self.begin
        q = other.begin
        while p != None and q != None:
            if p.value != q.value:
                return False
            p = p.next
            q = q.next
        return p == None and q == None
    def __ne__(self, other):
        return not self == other
    def __repr__(self):
        return "[" + ", ".join(str(x) for x in self) + "]"
    def __str__(self):
        return repr(self)
    def __contains__(self, value):
        for x in self:
            if x == value:
                return True
        return False
    def __delitem__(self, index):
        if index == 0:
            self.begin = self.begin.next
        else:
            p = self.begin
            for i in range(index-1):
                if p == None:
                    raise IndexError
                p = p.next
            if p == None or p.next == None:
                raise IndexError
            p.next = p.next.next
    def __reversed__(self):
        novy = LinkedList()
        p = self.begin
        while p != None:
            novy.prepend(p.value)
            p = p.next
        return novy
    def __bool__(self):
        return self.begin != None

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




