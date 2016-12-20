from collections import deque
import copy

memo = set()
def is_valid(items, floor):
    if floor < 0 or floor > 3: return False
    if str(items) + str(floor) in memo: return False

    memo.add(str(items) + str(floor))

    not_paired = []
    for x, y in items:
        if x != y:
            not_paired.append(x)
    for x, y in items:
        if y in not_paired: return False
    return True

def possible_moves(items, floor):
    moves = []
    for i in range(len(items)):
        for j in range(2):
            if floor == items[i][j]:
                m1 = copy.deepcopy(items)
                m1[i][j] += 1
                m1.sort()
                moves.append((m1, floor + 1))

                m2 = copy.deepcopy(items)
                m2[i][j] -= 1
                m2.sort()
                moves.append((m2, floor - 1))

    for i in range(len(items)):
        for j in range(i, len(items)):
            for k in range(4):
                k1 = k // 2
                k2 = k % 2

                if i == j and k1 == k2: continue
                if items[i][k1] == floor and items[j][k2] == floor:
                    m1 = copy.deepcopy(items)
                    m1[i][k1] += 1
                    m1[j][k2] += 1
                    m1.sort()
                    moves.append((m1, floor+1))

                    m2 = copy.deepcopy(items)
                    m2[i][k1] -= 1
                    m2[j][k2] -= 1
                    m2.sort()
                    moves.append((m2, floor-1))
    return [(m, flr) for m, flr in moves if is_valid(m, flr)]


def number_of_moves(items):
    q = deque()
    q.append((items, 0, 0))
    while q:
        items, floor, moves = q.popleft()
        top = True
        for i in items:
            if i != [3, 3]:
                top = False
                break
        if top: return moves

        possible = possible_moves(items, floor)
        for itm, flr in possible:
            q.append((itm, flr, moves + 1))

in1 = [[0, 0], [0, 1], [0, 1], [2, 2], [2, 2]]
# generators and microchips by floors
in2 = copy.deepcopy(in1) + [[0, 0], [0, 0]]

print('#1', number_of_moves(in1))
print('#2', number_of_moves(in2))
