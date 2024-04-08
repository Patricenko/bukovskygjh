for t in range(int(input())):
    names = []
    winners = {}
    winnersord = []
    result = 0
    for h in range(int(input())):
        name = input()
        names.append(name)
        winners[name] = 0
    ka = int(input())
    for k in range(ka):
        name = input()
        winners[name] += 1
        winnersord.append(name)
    if 0 in winners.values():
        result = 0
    else:
        odd = 0
        najmenej_indexy = [i for i, e in enumerate(winnersord) if e == min(winners, key=winners.get)]
        najmenej = len(winnersord[:max(najmenej_indexy)])
        for i in range(1, len(najmenej_indexy)):
            diff = najmenej_indexy[i] - najmenej_indexy[i-1]
            najmenej = min(najmenej, diff)
        if ka % 2 == 1: odd = 1
        if najmenej > 1:
            result = (len(winnersord)-odd) // (najmenej-1)
        else: result = len(winnersord)-odd
    print(result)
