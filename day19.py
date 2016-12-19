number = [i for i in range(1, 3001330+1)]
# number = [i for i in range(1, 10)]
number2 = number[:]

last = len(number) % 2 != 0

while len(number) > 1:
    next_last = len(number) % 2 != last
    number = [j for i, j in enumerate(number) if i % 2 != last]
    last = next_last

print('#1', number[0])

number = number2

while len(number) > 1:
    pop = set()
    last = 0
    for i in range(len(number) // 2):
        last = number[i]
        pop.add(number[(2 * i + (len(number) - i) // 2) % len(number)])

    number = [i for i in number if i not in pop]
    if len(number) == 1: break
    pop = set()
    start = number.index(last) + 1

    for i in range(start, len(number)):
        pop.add(number[(i + (len(number) + i - start) // 2) % len(number)])
    number = [i for i in number if i not in pop]

print('#2', number[0])
