from collections import deque

# nodes are arranged in rectangle height x width
height = 30
width = 33

nodes = []
nodes2 = [[] for i in range(height)]
i = 0
while True:
    try: line = input()
    except: break
    if not line: break
    space, used, avail, perc = (int(i[:-1]) for i in line.split()[1:])
    nodes.append([used, avail, space, i])
    nodes2[i % height].append([used, space])
    i += 1

nodes.sort(key=lambda x: x[1], reverse=True)
count = 0

for i in range(len(nodes)):
    if nodes[i][0]:
        for j in range(len(nodes)):
            if nodes[j][1] >= nodes[i][0]:
                if nodes[j][3] != nodes[i][3]:
                    count += 1
            else:
                break

print('#1', count)

# NOTE: second part does not work in reality. It works for my input.
nodes = nodes2
path = reversed([(0, i) for i in range(width-1)])
target = (0, width-1)

for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        if nodes[i][j][0] == 0:
            start = (i, j)

len_of_path = 0
for goal in path:
    q = deque()
    q.append((*start, 0))
    visited = set()
    while q:
        y, x, moves = q.popleft()

        if (y, x) == target: continue

        if (y, x) == goal:
            len_of_path += moves
            # print(moves)
            break

        if (y, x) in visited: continue
        visited.add((y, x))

        # if data is too big to fit in node x0, y0
        if y > 0 and nodes[y-1][x][0] < nodes[0][0][1]:
            q.append((y-1, x, moves+1))
        if x > 0 and nodes[y][x-1][0] < nodes[0][0][1]:
            q.append((y, x-1, moves+1))
        if y < height-1 and nodes[y+1][x][0] < nodes[0][0][1]:
            q.append((y+1, x, moves+1))
        if x < width-1 and nodes[y][x+1][0] < nodes[0][0][1]:
            q.append((y, x+1, moves+1))

    start = target
    target = goal
    len_of_path += 1

print('#2', len_of_path)
