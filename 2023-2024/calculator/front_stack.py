#modul
class TItem:
    def __init__(self, info):
        self.info = info
        self.next = None
class TFront: #rad queue - enqueue, deque
    def __init__(self):
        self.begin = None
    def dequeue(self):
        if self.begin is not None:
            p = self.begin
            self.begin = self.begin.next
            return p.info
    def enqueue(self, info):
        if self.begin is None:
            self.begin = TItem(info)
        else:
            p = self.begin
            while p.next is not None:
                p = p.next
            p.next = TItem(info)
    def printme(self):
        p = self.begin
        while p.next is not None:
            print(p.info, end = ", ")
            p = p.next
    def is_empty(self):
        return True if self.begin is None else False

#queue = TFront()
#for i in range(40):
#    queue.enqueue(i)
#queue.printme()
#print("\n")
#queue.dequeue()
#queue.printme()
#print("\n")
#print(queue.is_empty())

class Tstack:
    def __init__(self):
        self.begin = None

    def is_empty(self):
        if self.begin == None:
            return True
        else:
            return False

    def push(self, info):
        if self.begin == None:
            self.begin = TItem(info)
        else:
            p = self.begin
            self.begin = TItem(info)
            self.begin.next = p

    def pop(self):
        p = self.begin
        if p == None:
            return None

        else:
            p = self.begin
            x = p.info
            p.info = None
            self.begin = p.next
            p.next = None
            return (x)

    def write(self):
        p = self.begin
        while p != None:
            print(p.info)
            p = p.next