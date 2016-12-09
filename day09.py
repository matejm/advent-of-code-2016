import re

def expand(s):
    new_string = ''
    i = 0
    for m in re.finditer(r'(\([0-9]+x[0-9]+\))', string):
        a, b = m.span()
        if i > a: continue

        length, num = [int(i) for i in re.findall(r'[0-9]+', m.group(0))]
        new_string += string[i : a]
        new_string += string[b : b + length] * num
        i = b + length

    new_string += string[i:]
    if i != 0:
        return new_string

string = input()
string = expand(string)
l = len(string)
print('#1', l)

while True:
    string = expand(string)
    if string is None: break
    l = len(string)
    print(l)
print(l)
