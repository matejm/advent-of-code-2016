triangles = []
while True:
    try: line = input()
    except: break
    if not line: break
    line = [int(i) for i in line.split()]
    triangles.append(line)

possible = 0
for a, b, c in triangles:
    if a + b > c and a + c > b and b + c > a:
        possible += 1
print('#1', possible)

possible = 0
for i in range(0, len(triangles), 3):
    for a, b, c in zip(triangles[i], triangles[i + 1], triangles[i + 2]):
        if a + b > c and a + c > b and b + c > a:
            possible += 1
print('#2', possible)
