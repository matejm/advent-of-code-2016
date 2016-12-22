nodes = []
i = 0
while True:
    try: line = input()
    except: break
    if not line: break
    space, used, avail, perc = (int(i[:-1]) for i in line.split()[1:])
    nodes.append([used, avail, space, i])
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
