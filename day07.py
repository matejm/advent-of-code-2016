import re

def validate(s):
    for i in range(len(s)-3):
        if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
            return True
    return False

def find_aba(s):
    st = set()
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i] == s[i+2]:
            st.add(s[i : i+3])
    return st

def find_bab(s):
    st = find_aba(s)
    st = set((i[1] + i[0] + i[1] for i in st))
    return st

ips = []
while True:
    try: line = input()
    except: break
    if not line: break
    ips.append(line)

tls = 0
ssl = 0
for ip in ips:
    b = False
    B = True
    aba = set()
    bab = set()

    for i in re.findall(r'\[([a-z]+)\]', ip):
        bab |= find_bab(i)
        if validate(i): B = False
    for i in re.findall(r'\]([a-z]*)', ip) + re.findall(r'^([a-z]*)', ip):
        b |= validate(i)
        aba |= find_aba(i)

    if b and B: tls += 1
    if aba & bab: ssl += 1

print('#1', tls)
print('#2', ssl)
