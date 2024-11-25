import random
def randomize(n: int) -> list:
    return [random.randint(1, 99) for _ in range(n)]

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


p = randomize(10)

