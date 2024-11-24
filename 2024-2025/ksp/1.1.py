vstup = [1] + [int(x) for x in input()]
steps = 0
for i in range(len(vstup)-1):
    steps += 1
    if abs(vstup[i] - vstup[i+1]) >= 5:
        steps += 10 - abs(vstup[i] - vstup[i+1])
    else:
        steps += abs(vstup[i] - vstup[i+1])
print(steps)