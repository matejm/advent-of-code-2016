import hashlib
from queue import Queue

passcode = 'bwnlcvfs'
queue = Queue()
queue.put(('', 0, 0))
last = ''
first = True

while not queue.empty():
    path, x, y = queue.get()
    print(len(path))

    if x == 3 and y == 3:
        last = path
        if first: print('#1', path)
        first = False
        continue

    s = passcode + path
    m = hashlib.md5()
    m.update(s.encode('utf8'))
    up, down, left, right = m.hexdigest()[:4]

    if up in 'bcdef' and y > 0:
        queue.put((path + 'U', x, y-1))
    if down in 'bcdef' and y < 3:
        queue.put((path + 'D', x, y+1))
    if left in 'bcdef' and x > 0:
        queue.put((path + 'L', x-1, y))
    if right in 'bcdef' and x < 3:
        queue.put((path + 'R', x+1, y))

print('#2', len(last))
