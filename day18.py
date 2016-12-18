# true if solving for first star
first = True

puzzle_input = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'

field = [[i == '.' for i in puzzle_input]]

for i in range(40 - 1 if first else 400000 - 1):
    if i % 10000 == 0: print(i)
    line = []
    for j in range(len(field[0])):
        left, center, right = True, field[i][j], True
        if j > 0: left = field[i][j-1]
        if j+1 < len(field[0]): right = field[i][j+1]

        if ((left == center and right != center) or (right == center and left != center)):
            line.append(False)
        else:
            line.append(True)
    field.append(line)

print('#1' if first else '#2', sum([sum(line) for line in field]))
