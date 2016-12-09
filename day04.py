from collections import defaultdict

def caesar_chiper(char, n):
    c = ord(char) - ord('a')
    c += n
    c %= 26
    c += ord('a')
    return chr(c)

rooms = []
while True:
    try: line = input()
    except: break
    if not line: break
    i = line.rfind('-')
    j = line.find('[')
    line = line[:i], int(line[i + 1 : j]), line[j+1 : -1]
    rooms.append(line)

real_sum = 0
for name, sector, checksum in rooms:
    count = defaultdict(int)

    decrypted_name = ''.join([caesar_chiper(i, sector) if i != '-' else ' ' for i in name])
    if 'northpole' in decrypted_name:
        print('#2', decrypted_name, sector)

    name = name.replace('-', '')
    for char in name:
        count[char] += 1
    name = list(set(name))
    name = sorted(name, key=lambda x: ord(x) - count[x] * 128)
    if list(checksum) == name[:5]:
        real_sum += sector

print('#1', real_sum)
