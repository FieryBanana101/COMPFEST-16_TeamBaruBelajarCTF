from pwn import *

io = remote("challenges.ctf.compfest.id",20015)

ciphertext = ''

io.recvuntil(">> ")
io.sendline('1')
io.recvuntil("Message: ")
io.sendline("a"*7 + "COMPFEST1")
io.recvuntil(': ')
temp = io.recvline().decode().rstrip()
ciphertext += temp[0:32]

io.recvuntil(">> ")
io.sendline('1')
io.recvuntil("Message: ")
io.sendline("6" + "a"*15)
io.recvuntil(': ')
ciphertext += io.recvline().decode()[0:32]


io.recvuntil(">> ")
io.sendline('1')
io.recvuntil("Message: ")
io.sendline('\x01'*16)
io.recvuntil(': ')
ciphertext += io.recvline().decode()[0:32]


io.recvuntil(">> ")
io.sendline('2')
io.recvuntil(": ")
io.sendline(ciphertext)

print("Flag:", io.recvline().decode().rstrip())
io.interactive()
