# 9.9.2024
import random
from linkedlist import *
t = 21

def randomize(n: int) -> list:
    return [random.randint(1, 99) for _ in range(n)]
def max_sort(p: list, n = t) -> list:
    global max_p
    for i in range(n):
        if i == 0:
            max_p = 0
        if p[i] >= p[max_p]:
            max_p = i
    p[max_p], p[n-1] = p[n-1], p[max_p]
    if n > 1:
        max_sort(p, n-1)
    return p

def bubble_sort(p: list, n = t) -> list:
    for i in range(n):
        for j in range(n-1-i):
            if p[j] > p[j+1]:
                p[j], p[j+1] = p[j+1], p[j]
    return p
def heap_sort(p):
    # i ma deti 2i+1 a 2i+2, strom

    def heapify(p, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and p[i] < p[left]:
            largest = left
        if right < n and p[largest] < p[right]:
            largest = right
        if largest != i:
            p[i], p[largest] = p[largest], p[i]
            heapify(p, n, largest)
        return

    for i in range(len(p)//2-1, -1, -1):
        heapify(p, len(p), i)
    for i in range(len(p)-1, 0, -1):
        p[i], p[0] = p[0], p[i]
        heapify(p, i, 0)
    return p
def quick_sort(p):
    if len(p) <= 1:
        return p
    pivot = p.pop(0)
    left = []
    right = []
    for i in p:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(p):
    def merge(l, r):
        p = []
        while l and r:
            if l[0] < r[0]:
                p.append(l.pop(0))
            else:
                p.append(r.pop(0))
        return p + l + r
    if len(p) <= 1:
        return p
    l = merge_sort(p[:len(p)//2])
    r = merge_sort(p[len(p)//2:])
    return merge(l, r)
def toRPN(arr):
    # +-*/^()
    stack = []
    result = []
    for i in arr:
        if i in "+-":
            while stack and stack[-1] in "+-*/^":
                result.append(stack.pop())
            stack.append(i)
        elif i in "*/^":
            while stack and stack[-1] in "*/^SSSSSSSSSSSSSSSSSS":
                result.append(stack.pop())
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(i)
    while stack:
        result.append(stack.pop())
    return result


def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
        return arr

    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def radix_sort_binary(arr):
    max_bits = len(bin(max(arr)))-2
    for bit in range(max_bits):
        zeroes = []
        ones = []
        for num in arr:
            if num & (1 << bit):
                ones.append(num)
            else:
                zeroes.append(num)
        arr = zeroes + ones
    return arr


def radix_sort_binary_ll(arr):
    max_bits = len(bin(max(arr))) - 2
    ll = LinkedList.from_list(arr)

    for bit in range(max_bits):
        zeroes = LinkedList()
        ones = LinkedList()
        current = ll.begin

        while current:
            if current.value & (1 << bit):
                ones.append(current.value)
            else:
                zeroes.append(current.value)
            current = current.next

        zeroes.concat(ones)
        ll = zeroes

    return ll.to_list()





# Example usage
p = randomize(t)
print("Unsorted:         ", p)
print("Radix Sorted:     ", radix_sort_binary(p))
print("Radix Sorted LL:  ", radix_sort_binary_ll(p))
