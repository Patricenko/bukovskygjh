import sys
sys.setrecursionlimit(100)
def play(steps, times, counter=0, start=0):
    for i in range(start, times):
        if steps[i] == 1:
            print(steps)
            if i == times-1:
                return print(counter)
            steps[i] = 0
        else:
            steps[i] = 1
            print(steps)
            return play(steps, times, counter+1)

def play(step, times):
    counter = 0
    i = 0
    while i < times:
        if steps[i] == 1:
            steps[i] = 0
            i += 1
        else:
            steps[i] = 1
            i = 0
            counter += 1
    return print(counter)

times = int(input())
steps = list(map(int, input().split()))
vladko_steps(steps, times)
