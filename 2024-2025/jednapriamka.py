def is_on_line(p: list) -> bool:
    if len(p) < 3:
        return True
    for i in range(2, len(p)):
        if (p[i][0] - p[0][0]) * (p[1][1] - p[0][1]) != (p[1][0] - p[0][0]) * (p[i][1] - p[0][1]):
            return False
    return True
p = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]
print(is_on_line(p))
p2 = [[1, 2], [2, 4], [3, 6], [4, 7]]
print(is_on_line(p2))