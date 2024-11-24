import math
x = [int(i) for i in input().strip()]
steps = 0
print(x)
for i in range(1,len(x)+1):
    if i == len(x):
        steps += 1
        break
    if x[i-1] < 5 and x[i] >= 5:
        steps += abs((10-x[i])+x[i-1])
    elif x[i-1] >= 5 and x[i] < 5:
        steps += abs((10-x[i-1])+x[i])
    else:
        steps += abs(x[i]-x[i-1])
print(steps)