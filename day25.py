commands = []
while True:
    try: line = input()
    except: break
    if not line: break
    commands.append(line.split())

for starting_a in range(155, 160):
    d = {'a': starting_a, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    out = []

    while len(out) < 100:
        if commands[i][0] == 'inc' and commands[i+1][0] == 'dec' and commands[i+2][0] == 'jnz' and commands[i+1][1] == commands[i+2][1] and commands[i+2][2] == '-2':
            d[commands[i][1]] += d[commands[i+1][1]]
            d[commands[i+1][1]] = 0
            i += 3
            continue
        elif commands[i][0] == 'cpy':
            a, b = commands[i][1:]
            if a.isalpha():
                d[b] = d[a]
            elif b.isalpha():
                d[b] = int(a)
        elif commands[i][0] == 'inc':
            d[commands[i][1]] += 1
        elif commands[i][0] == 'dec':
            d[commands[i][1]] -= 1
        elif commands[i][0] == 'jnz':
            a, b = commands[i][1:]
            if a.isalpha():
                if d[a] != 0:
                    i += (d[b] if b.isalpha() else int(b)) - 1
            else:
                if int(a) != 0:
                    i += (d[b] if b.isalpha() else int(b)) - 1
        elif commands[i][0] == 'tgl':
            a = commands[i][1]
            if a.isalpha(): a = d[a]
            else: a = int(a)
            if i + a >= 0 and i + a < len(commands):
                command = commands[i + a][0]
                if command == 'inc': command = 'dec'
                elif command == 'dec': command = 'inc'
                elif command == 'jnz': command = 'cpy'
                elif command == 'cpy': command = 'jnz'
                elif command == 'tgl': command = 'inc'
                commands[i + a][0] = command
        elif commands[i][0] == 'out':
            out.append(d[commands[i][1]])
        i += 1
    if out == [i % 2 for i in range(100)]:
        print(starting_a)
