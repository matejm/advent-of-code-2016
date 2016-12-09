ways = 'NESW'

def change_facing(facing, direction):
    if direction == 'R': change = 1
    else: change = -1
    a = ways.find(facing) + change
    return ways[a % 4]

facing = 'N'
pos = [0, 0]
directions = input().split(', ')
visited = [[False for i in range(1000)] for j in range(1000)]
visited_twice = None
for i in directions:
    facing = change_facing(facing, i[0])
    dis = int(i[1:])
    for j in range(dis):
        print(pos, visited[pos[0]][pos[1]])
        if visited_twice is None and visited[pos[0]][pos[1]]:
            visited_twice = pos[:]
        visited[pos[0]][pos[1]] = True

        if facing == 'N': pos[1] += 1
        elif facing == 'E': pos[0] += 1
        elif facing == 'S': pos[1] -= 1
        elif facing == 'W': pos[0] -= 1

print('#1', abs(pos[0]) + abs(pos[1]))
print('#2', abs(visited_twice[0]) + abs(visited_twice[1]))
