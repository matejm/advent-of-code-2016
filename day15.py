# solving first start
first = True

# puzzle input
# disc is represented by tuple (number of positions, starting position)
discs = [(7, 0), (13, 0), (3, 2), (5, 2), (17, 0), (19, 7)]

if not first:
    discs.append((11, 0))

start = 0
while True:
    time = start
    success = True
    for disc in discs:
        time += 1
        if (time + disc[1]) % disc[0]:
            success = False
            break
    if success:
        break
    start += 1

print('#{}'.format(1 if first else 2), start)
