instructions = []
while True:
    try:
        moves = input()
    except: break
    if not moves: break
    instructions.append(moves)

keypad1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
keypad2 = ['       ', '   1   ', '  234  ', ' 56789 ', '  ABC  ', '   D   ', '       ']
current1 = [1, 1]
current2 = [3, 1]
code1 = []
code2 = []

for moves in instructions:
    for move in moves:
        if move == 'U':
            current1[0] = max(0, current1[0] - 1)
            if keypad2[current2[0] - 1][current2[1]] != ' ':
                current2[0] -= 1
        elif move == 'L':
            current1[1] = max(0, current1[1] - 1)
            if keypad2[current2[0]][current2[1] - 1] != ' ':
                current2[1] -= 1
        if move == 'D':
            current1[0] = min(2, current1[0] + 1)
            if keypad2[current2[0] + 1][current2[1]] != ' ':
                current2[0] += 1
        if move == 'R':
            current1[1] = min(2, current1[1] + 1)
            if keypad2[current2[0]][current2[1] + 1] != ' ':
                current2[1] += 1

    code1.append(keypad1[current1[0]][current1[1]])
    code2.append(keypad2[current2[0]][current2[1]])

print('#1', ''.join((str(i) for i in code1)))
print('#2', ''.join((str(i) for i in code2)))
