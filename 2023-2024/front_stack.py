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

class TStack:
    def __init__(self):
        self.begin = TItem("head")
        self.size = 0
    def push(self, info):
        self.begin = TItem(info)
    def enqueue(self, info):
        if self.begin is None:
            self.begin = TItem(info)
        else:
            p = self.begin
            while p.next is not None:
                p = p.next
            p.next = TItem(info)
    def is_empty(self):
        return self.size == 0
    def push(self, info):
        item = TItem(info)
        item.next = self.begin.next
        self.begin.next = item
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        p = self.begin.next
        self.begin.next = self.begin.next.next
        self.size -= 1
        return p.info
    def printme(self):
        p = self.begin.next
        while p.next is not None:
            print(p.info, end = ", ")
            p = p.next