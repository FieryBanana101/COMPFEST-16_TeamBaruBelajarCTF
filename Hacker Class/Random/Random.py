import random
import string

enc = b'!vP3\xc2\x91\xc2\x89\x11\x1f\x06C\x17_\x19t)\xc2\x929\x06li\x1d\x1f\xc2\x88*\x19E+4E\x16\x07v1S$\x1a c\x1flcr4> 3vlt\xc2\x85Yj-$0 '.decode()

for seed in range(0, 334):
    random.seed(seed)
    flag = ''
    for i in enc:
        char = ord(i)
        offset = random.randint(1,10)
        MyFriend = random.randint(1, 127)
        addExtra = random.randint(0,1)
        if addExtra :
            char -= 22
        char ^= MyFriend
        char += offset
        if char in [ord(i) for i in string.printable]:
            flag += chr(char)

    if "COMPFEST16" in flag:
        print(f"Possible flag: {flag}")
