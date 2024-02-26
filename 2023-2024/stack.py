class Titem:
    def __init__(self, info):
        self.info = info
        self.next = None


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
            self.begin = Titem(info)
        else:
            p = self.begin
            self.begin = Titem(info)
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