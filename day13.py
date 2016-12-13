from queue import Queue
from collections import defaultdict

# True if solving part 1, else False
part1 = False

def calc(x, y):
    global favourite
    value = x*x + 3*x + 2*x*y + y + y*y + favourite
    return ('{:b}'.format(value)).count('1') % 2

visited = set()
favourite = int(input())
q = Queue()
q.put((1, 1, 0))
c = 0

while not q.empty():
    x, y, dis = q.get()

    if x == 31 and y == 39 and part1:
        print('#1', dis)
        break

    if calc(x, y) == 0 and (x, y) not in visited:
        c+=1
    visited.add((x, y))

    if dis > 50 and not part1:
        print('#2', c)
        break

    if calc(x, y) == 0:
        if x > 0 and (x-1, y) not in visited:
            q.put((x-1, y, dis+1))
        if y > 0 and (x, y-1) not in visited:
            q.put((x, y-1, dis+1))
        if (x+1, y) not in visited:
            q.put((x+1, y, dis+1))
        if (x, y+1) not in visited:
            q.put((x, y+1, dis+1))
