from pwn import *

r = remote("challenges.ctf.compfest.id", 9009)

r.recvuntil('\n')
r.sendline("5432,22")
r.recvuntil('\n')
r.sendline("server:changeme")
r.recvuntil('\n')
r.sendline("cafecoagroindustrialdelpacfico")
r.recvuntil('\n')
r.sendline("penalties")
r.recvuntil('\n')
r.sendline('Lyubov Pryadko')
r.interactive()
