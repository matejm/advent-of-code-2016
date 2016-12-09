display = [[False for i in range(50)] for j in range(6)]

commands = []
while True:
    try: line = input()
    except: break
    if not line: break
    commands.append(line)

for command in commands:
    if command[:4] == 'rect':
        i, j = command.find(' '), command.find('x')
        a = command[i+1 : j]
        b = command[j+1 :]
        for i in range(int(b)):
            for j in range(int(a)):
                display[i][j] = True
    elif 'column' in command:
        i = command.find('=')
        j = i + 2
        if command[j] != ' ': j += 1
        k = command.rfind(' ')
        col = int(command[i+1 : j])
        by = int(command[k+1 :])
        l = []
        for i in range(len(display)):
            l.append(display[i][col])
        l = l[-by:] + l[:-by]
        for i in range(len(display)):
            display[i][col] = l[i]
    elif 'row' in command:
        i = command.find('=')
        j = i + 2
        if command[j] != ' ': j += 1
        k = command.rfind(' ')
        row = int(command[i+1 : j])
        by = int(command[k+1 :])
        l = []
        for i in range(len(display[0])):
            l.append(display[row][i])
        l = l[-by:] + l[:-by]
        for i in range(len(display[0])):
            display[row][i] = l[i]

count = 0
for line in display:
    print(''.join(['#' if i else '.' for i in line]))
    count += sum(line)
print('#1', count)
