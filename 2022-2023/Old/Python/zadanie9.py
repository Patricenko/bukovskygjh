def move(pos, direction):
    if direction == "U":
        pos[1] += 1
    elif direction == "D":
        pos[1] -= 1
    elif direction == "L":
        pos[0] -= 1
    elif direction == "R":
        pos[0] += 1
    return pos


def follow(tail, head, direction):
    if is_adjacent(tail, head):
        return tail
    (tail_x, tail_y), (head_x, head_y) = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail


def is_adjacent(tail, head):
    return all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)])


head = [0, 0]
tail = head.copy()
one = head.copy()
two = head.copy()
three = head.copy()
four = head.copy()
five = head.copy()
six = head.copy()
seven = head.copy()
eight = head.copy()
nine = head.copy()

part_one = {tuple(head)}
part_two = {tuple(head)}


with open("zadanie9.txt") as fp:
    for motion in fp:
        d, n = [int(x) if x.isnumeric() else x for x in motion.rstrip().split()]
        for i in range(n):

            head = move(head, d)

            tail = follow(tail, head, d)
            part_one.add(tuple(tail))

            one = follow(one, head, d)
            two = follow(two, one, d)
            three = follow(three, two, d)
            four = follow(four, three, d)
            five = follow(five, four, d)
            six = follow(six, five, d)
            seven = follow(seven, six, d)
            eight = follow(eight, seven, d)
            nine = follow(nine, eight, d)
            part_two.add(tuple(nine))

print("Part 1:", len(part_one), "\nPart 2:", len(part_two))
