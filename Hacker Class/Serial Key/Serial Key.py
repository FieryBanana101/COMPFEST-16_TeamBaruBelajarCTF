from pwn import *

key = ['_' for i in range(24)]
for i in range(4,24,5):
    key[i] = chr(45)

key[10] = 'C'
key[11] = 'F'
key[12] = '1'
key[13] = '6'
key[0] = 'A'
key[5] = 'B'
key[15] = 'D'
key[20] = 'E'

r = remote('challenges.ctf.compfest.id', 20012)

cnt = 0
while cnt <= 99:
    r.recvuntil("==> ")
    curr_str = str(cnt)
    for i in range(-1,-len(curr_str)-1,-1):
        key[i] = curr_str[i]
    serial = ''
    for i in range(24):
        if key[i] == '_':
            serial += '0'
        else:
            serial += key[i]
    r.sendline(serial)
    cnt += 1

print("Flag: ", r.recvuntil('}'))
