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

def expand2(reversed_s):
    total_len = 0
    stack = [(0, 0, 0)]
    for m in re.finditer(r'(\)[0-9]+x[0-9]+\()', reversed_s):
        a, b = m.span()
        num, length = (i for i in re.findall(r'[0-9]+', m.group(0)))
        num = int(num[::-1])
        length = int(length[::-1])
        ln = length * num

        pops = set()
        for i in range(len(stack)):
            a2, b2, ln2 = stack[i]
            if a2 >= a - length:
                ln -= (b2-a2) * num
                ln += ln2 * num
                pops.add(i)
        stack = [j for i, j in enumerate(stack) if i not in pops]
        stack.append((a - length, b, ln))

    stack.append((len(reversed_s), len(reversed_s), 0))
    for i in range(len(stack)-1):
        total_len += stack[i+1][0] - stack[i][1]
        total_len += stack[i][2]

    return total_len


string = input()
l2 = expand2(string[::-1])
string = expand(string)
l = len(string)
print('#1', l)
print('#2', l2)
