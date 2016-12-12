commands = []
while True:
    try: line = input()
    except: break
    if not line: break
    commands.append(line.split())

# first
d = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# second
d = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

i = 0
while i < len(commands):
    if commands[i][0] == 'cpy':
        a, b = commands[i][1:]
        if a.isalpha():
            d[b] = d[a]
        else:
            d[b] = int(a)
    elif commands[i][0] == 'inc':
        d[commands[i][1]] += 1
    elif commands[i][0] == 'dec':
        d[commands[i][1]] -= 1
    elif commands[i][0] == 'jnz':
        a, b = commands[i][1:]
        if a.isalpha():
            if d[commands[i][1]] != 0:
                i += d[commands[i][2]] if commands[i][2].isalpha() else int(commands[i][2]) - 1
        else:
            if int(commands[i][1]) != 0:
                i += d[commands[i][2]] if commands[i][2].isalpha() else int(commands[i][2]) - 1
    i += 1

print(d['a'])
