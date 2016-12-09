import hashlib

door_id = input()
password1 = []
password2 = list('________')
pass2_count = 0

for i in range(10**10):
    s = door_id + str(i)

    m = hashlib.md5()
    m.update(s.encode('utf8'))

    if m.hexdigest()[:5] == '00000':
        print(s, m.hexdigest(), '{}%'.format((len(password1) + pass2_count) / 0.16))
        digit = m.hexdigest()[5]
        if len(password1) < 8:
            password1.append(digit)
        if digit in '01234567' and password2[int(digit)] == '_':
            password2[int(digit)] = m.hexdigest()[6]
            pass2_count += 1
        if len(password1) == 8 and pass2_count == 8:
            break

print('#1', ''.join(password1))
print('#2', ''.join(password2))
