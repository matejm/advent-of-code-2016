from collections import deque, defaultdict

with open('in') as f:
    maze = f.readlines()

open_pass = 0
checkpoints = 0
memo = defaultdict(set)

for i in range(len(maze)):
    maze[i] = list(maze[i])
    for j in range(len(maze[i])):
        c = maze[i][j]
        if c in '987654321':
            checkpoints += 1
            maze[i][j] = int(c) + 1
        elif c == '0':
            c = '.'
            start = (i, j)
        if c == '.':
            maze[i][j] = 0
            open_pass += 1
        elif c == '#' or c == '\n':
            maze[i][j] = 1

# fill blind alleys
for __ in range(10):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0 and (i, j) != start:
                count = 0
                if maze[i-1][j] == 1: count += 1
                if maze[i][j-1] == 1: count += 1
                if maze[i+1][j] == 1: count += 1
                if maze[i][j+1] == 1: count += 1
                if count >= 3:
                    maze[i][j] = 1
                    open_pass -= 1

for i in range(len(maze)):
    print(''.join([(str(k) if k != 1 else '■') if k != 0 else ' ' for k in maze[i]]))

target = 0
for i in range(checkpoints):
    target |= (1 << i)

queue = deque()
# y, x, number of visited, number of steps
queue.append((*start, 0, 0))
path_len = 0
start2 = []
b = True

while queue:
    y, x, num, step = queue.popleft()

    if maze[y][x] > 1:
        num |= 1 << (maze[y][x]-2)
        if num == target:
            start2.append((y, x, step))
            if b:
                print('#1', step)
                b = False

    # better or same score on same place with less or same steps
    if num in memo[(y, x)]: continue
    memo[(y, x)].add(num)

    if maze[y][x-1] != 1:
        queue.append((y, x-1, num, step+1))
    if maze[y][x+1] != 1:
        queue.append((y, x+1, num, step+1))
    if maze[y-1][x] != 1:
        queue.append((y-1, x, num, step+1))
    if maze[y+1][x] != 1:
        queue.append((y+1, x, num, step+1))

print('#1', path_len)

queue = deque()
# y, x, number of steps
for i in start2:
    queue.append(i)
memo = defaultdict(bool)

while queue:
    y, x, step = queue.popleft()
    # print(y, x, step)

    if (y, x) == start:
        path_len = step
        break

    # just check if visited
    if memo[(y, x)]: continue
    memo[(y, x)] = True

    if maze[y][x-1] != 1:
        queue.append((y, x-1, step+1))
    if maze[y][x+1] != 1:
        queue.append((y, x+1, step+1))
    if maze[y-1][x] != 1:
        queue.append((y-1, x, step+1))
    if maze[y+1][x] != 1:
        queue.append((y+1, x, step+1))

print('#2', path_len)
