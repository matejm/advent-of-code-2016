import re

def swap_position(s, x, y):
    s[x], s[y] = s[y], s[x]

def swap_letter(s, x, y):
    s2 = []
    for i in s:
        if i == x: s2.append(y)
        elif i == y: s2.append(x)
        else: s2.append(i)
    return s2

def rotate(s, direction, x):
    if direction == 'left':
        return s[x:] + s[:x]
    return s[-x:] + s[:-x]

def rotate_based_on_position(s, x):
    ind = s.index(x)
    if ind >= 4: ind += 1
    ind += 1
    ind %= len(s)
    return rotate(s, 'right', ind)

def rotate_based_on_position_reverse(s, x):
    s2 = s[:]
    for i in range(len(s)):
        s3 = rotate_based_on_position(s2, x)
        if s3 == s:
            return s2
        s2 = rotate(s2, 'right', 1)
    raise


def reverse_positions(s, x, y):
    return s[:x] + list(reversed(s[x : y+1])) + s[y+1:]

def move_position(s, x, y):
    c = s.pop(x)
    s = s[:y] + [c] + s[y:]
    return s

commands = []
while True:
    try: line = input()
    except: break
    if not line: break
    commands.append(line)

password = list('abcdefgh')

for i, c in enumerate(commands):
    if 'swap position' in c:
        x, y = (int(i) for i in re.findall(r'swap position ([0-9]+) with position ([0-9]+)', c)[0])
        swap_position(password, x, y)
    elif 'swap letter' in c:
        x, y = re.findall(r'swap letter ([a-z]) with letter ([a-z])', c)[0]
        password = swap_letter(password, x, y)
    elif 'rotate left' in c or 'rotate right' in c:
        direction, x = re.findall(r'rotate ([a-z]+) ([0-9]) step', c)[0]
        x = int(x) % len(password)
        password = rotate(password, direction, x)
    elif 'rotate based on position of letter' in c:
        x = re.findall(r'rotate based on position of letter ([a-z])', c)[0]
        password = rotate_based_on_position(password, x)
    elif 'reverse positions' in c:
        x, y = (int(i) for i in re.findall(r'reverse positions ([0-9]+) through ([0-9]+)', c)[0])
        password = reverse_positions(password, x, y)
    elif 'move position' in c:
        x, y = (int(i) for i in re.findall(r'move position ([0-9]+) to position ([0-9]+)', c)[0])
        password = move_position(password, x, y)

print('#1', ''.join(password))
password = list('fbgdceah')

for i, c in enumerate(reversed(commands)):
    if 'swap position' in c:
        x, y = (int(i) for i in re.findall(r'swap position ([0-9]+) with position ([0-9]+)', c)[0])
        swap_position(password, x, y)
    elif 'swap letter' in c:
        x, y = re.findall(r'swap letter ([a-z]) with letter ([a-z])', c)[0]
        password = swap_letter(password, x, y)
    elif 'rotate left' in c or 'rotate right' in c:
        direction, x = re.findall(r'rotate ([a-z]+) ([0-9]) step', c)[0]
        x = int(x) % len(password)
        direction = 'left' if direction == 'right' else 'right'
        password = rotate(password, direction, x)
    elif 'rotate based on position of letter' in c:
        x = re.findall(r'rotate based on position of letter ([a-z])', c)[0]
        password = rotate_based_on_position_reverse(password, x)
    elif 'reverse positions' in c:
        x, y = (int(i) for i in re.findall(r'reverse positions ([0-9]+) through ([0-9]+)', c)[0])
        password = reverse_positions(password, x, y)
    elif 'move position' in c:
        x, y = (int(i) for i in re.findall(r'move position ([0-9]+) to position ([0-9]+)', c)[0])
        password = move_position(password, y, x)


print('#2', ''.join(password))
