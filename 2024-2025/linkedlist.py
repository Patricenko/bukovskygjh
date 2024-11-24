class LinkedList():
    def __init__(self):
        self.begin = None
    def append(self, info):
        if self.begin == None:
            self.begin = TItem(info)
        else:
            p = self.begin
            while p.next != None:
                p = p.next
            p.next = TItem(info)
    def insert(self,pos,info):
        if self.begin == None:
            self.begin = TItem(info)
        else:
            pp = LinkedList()
            p = self.begin
            i = 0
            while p != None:
                if pos == i:
                    pp.append(info)
                else:
                    pp.append(p.info)
                    p = p.next
                i += 1
            self.begin = pp.begin

    def insert0(self,info):
        if self.begin == None:
            self.begin = TItem(info)
        else:
            p = self.begin
            self.begin = TItem(info)
            self.begin.next = p
    def vypis(self):
        p = self.begin
        while p != None:
            print(p.info)
            p = p.next
    def reverse(self, info):
        novy = LinkedList()
        p = self.begin
        while p != None:
            novy.insert0(p.info)
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
            cc.append(p.info)
            p = p.next
        return cc

