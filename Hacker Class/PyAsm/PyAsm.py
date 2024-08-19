from math import *
from pwn import *

x = [ord('_') for i in range(9)]

# x[7]+69 = 120
# x[3]^1337 = 1355
# x[0] // 22 = 5
# x[4] - 16 = 35
# x[8] << 3 = 832
# x[1] ** 2 = 9409
# x[6] * 7 = 693
# ~x[2] = -110
# x[5] = 107

x[7] = 120-69
x[3] = 1337 ^ 1355
x[0] = 5 * 22
x[4] = 16+35
x[8] = 832 // 8
x[1] = floor(sqrt(9409))
x[6] = 693 // 7
x[2] = ~(-110)
x[5] = 107

x.reverse()

password = ''
for i in x:
    password += chr(i)

io = remote("challenges.ctf.compfest.id",20011)

io.recvuntil(": ")
io.sendline(password)
io.recvuntil("flag: \n")

print("Flag:", io.recvuntil('}').decode())
