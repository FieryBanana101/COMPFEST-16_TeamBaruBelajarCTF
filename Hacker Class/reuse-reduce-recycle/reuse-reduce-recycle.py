from pwn import *
from tqdm import tqdm

r = remote("challenges.ctf.compfest.id", 20016)

r.recvuntil(">> ")
r.sendline('2')
r.recvuntil('Encrypted Message (hex): ')
enc_flag = r.recvuntil('\n').rstrip().decode()

flag = 'COMPFEST16{'

r.recvuntil('>> ')

while flag[-1] != '}':
    for char in tqdm(string.printable):
        r.sendline('1')
        r.recvuntil("Message: ")
        r.sendline(flag+char)
        r.recvuntil('Encrypted Message (hex): ')
        enc_plain = r.recvuntil('\n').rstrip().decode()
        r.recvuntil('>> ')

        same = True
        for i in range(0,len(flag+char)*2):
            if enc_plain[i] != enc_flag[i]:
                same = False
                break
                
        if same:
            flag += char
            break

print(flag)
