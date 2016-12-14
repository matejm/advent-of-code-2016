import hashlib
import re

# first problem
first = True

def hash(s):
    for i in range(2017):
        m = hashlib.md5()
        m.update(s.encode('utf8'))
        s = m.hexdigest()
    return s

key = input()
l = []
strings = []

for i in range(10**10):
    if i % 1000 == 0:
        print(i)
    s = key + str(i)

    if first:
        m = hashlib.md5()
        m.update(s.encode('utf8'))
        m = m.hexdigest()
    else:
        m = hash(s)

    last_c, lastlast_c = '', ''
    for c in m:
        if last_c == lastlast_c and last_c == c:
            l.append((i+1000, last_c[0]))
            break
        lastlast_c = last_c
        last_c = c

    q = re.search(r'(00000)|(11111)|(22222)|(33333)|(44444)|(55555)|(66666)|(77777)|(88888)|(99999)|(aaaaa)|(bbbbb)|(ccccc)|(ddddd)|(eeeee)|(fffff)', m)
    if q:
        delete = set()
        for j in range(len(l)-1):
            if l[j][0] < i:
                delete.add(j)
            elif q.group(0)[0] == l[j][1]:
                strings.append((m, l[j][0]-1000))
                if len(strings) >= 64:
                    break
        if len(strings) >= 64:
            break
        if delete:
            l = [l[k] for k in range(len(l)) if k not in delete]

print('#{:d}'.format(1 if first else 2), sorted(strings, key=lambda x: x[1])[63][1])
