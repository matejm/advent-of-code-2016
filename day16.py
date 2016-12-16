def checksum(s):
    cs = ''
    for i in range(0, len(s), 2):
        cs += '01'[s[i] == s[i+1]]
    if len(cs) % 2 == 0:
        return checksum(cs)
    return cs

curve = '10001110011110000'
target = 272
target2 = 35651584

while len(curve) < target2:
    curve2 = ''.join(['1' if i == '0' else '0' for i in reversed(curve)])
    curve += '0' + curve2

print(checksum(curve[:target]))
print(checksum(curve[:target2]))
