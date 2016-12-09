from collections import defaultdict

messages = []
while True:
    try: line = input()
    except: break
    if not line: break
    messages.append(line)

message1 = []
message2 = []
for i in range(len(messages[0])):
    count = defaultdict(int)
    for j in range(len(messages)):
        count[messages[j][i]] += 1
    most_frequent = max(count.items(), key=lambda x: x[1])
    least_frequent = min(count.items(), key=lambda x: x[1])
    message1.append(most_frequent[0])
    message2.append(least_frequent[0])

print('#1', ''.join(message1))
print('#2', ''.join(message2))
