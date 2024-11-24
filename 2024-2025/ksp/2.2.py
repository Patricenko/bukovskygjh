def play(step, times):
    counter = 0
    i = 0
    while i < times:
        if steps[i] == 1:
            i += 1
        else:
            steps[i] = 1
            counter += 1
            i += 1
    return print(counter)


times = int(input())
steps = list(map(int, input().split()))
play(steps, times)