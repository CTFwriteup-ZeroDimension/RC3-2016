key = b':"AL_RT^L*.?+6/46'
v = b'\x65\x62\x6D\x61\x72\x61\x68' *3
v = v[::-1]
mod = 7
passwd = []

for a, b in zip(v, key):
    passwd.append(chr(a^b))
print(''.join(passwd))
