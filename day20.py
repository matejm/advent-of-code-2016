
data = []
while True:
    try: line = input()
    except: break
    if not line: break
    data.append(tuple(int(i) for i in line.split('-')))

data.sort()
i = 0
count = 0
first = True
end = 0
valid = 4294967295

while i < len(data):
    while i < len(data) and data[i][0] <= end:
        end = max(end, data[i][1])
        i += 1

    if i == len(data):
        count += valid - end
        break

    count += data[i][0] - end - 1
    end = data[i][1]

    if first:
        first = False
        print('#1', end + 1)

print('#2', count)
