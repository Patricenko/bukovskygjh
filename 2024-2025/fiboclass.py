class Fibo:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.i = 0
    class FiboIterator:
        def __init__(self, n):
            self.n = n
            self.a = 0
            self.b = 1
            self.i = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.i < self.n:
                self.i += 1
                self.a, self.b = self.b, self.a+self.b
                return self.a
            else:
                raise StopIteration
    def __iter__(self):
        return self.FiboIterator(self.n)


p = Fibo(5)
for i in p:
    for j in p:
        print(j)