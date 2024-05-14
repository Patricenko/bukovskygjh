# Description: Pravidla slova
import random
class Analyse:
    class Node:
        def __init__(self, value = None):
            self.value = value
            self.ways = {}
    def __init__(self):
        self.begin = None
        self.vrcholy = {}
        self.pravidla = {}
        self.end = None
        self.create()
    def create(self):
        with open("rules.txt","r") as f:
            text = f.readlines()
            text = [riadok.strip() for riadok in text]
            vrcholy = text[0]
            zac = text[1]
            prav = text[2].split()
            kon = text[3]
        for p in vrcholy:
            self.vrcholy[p] = self.Node()
        self.begin = zac
        for p in range(len(prav)):
            if p%2 == 0:
                self.pravidla[prav[p]] = set(prav[p+1])
                self.vrcholy[prav[p]].ways = set(prav[p+1])
        self.end = kon
    def check(self, word) -> bool:
        if word[0] != self.begin: return False
        if word[-1] != self.end: return False
        for i in range(1,len(word)-1):
            if word[i] not in self.vrcholy: return False
            if word[i+1] not in self.vrcholy[word[i]].ways: return False
            return True
    def __str__(self):
        return f"Analyse({self.vrcholy})"

    def generate(self, limit):
        word = self.begin
        for i in range(limit):
            r = random.choice(list(self.vrcholy[word[-1]].ways))
            if r == self.end and i == limit-1:
                if 
                return word
        return word

analyza = Analyse()
print(analyza.check("abcar"))
print(analyza.generate(10))