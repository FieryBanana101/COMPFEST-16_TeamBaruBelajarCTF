import hashlib
import random
import string
from tqdm import tqdm

methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224']


def encrypt(x,method):
    hash_obj = hashlib.new(method)
    hash_obj.update(x.encode())
    return hash_obj.hexdigest()


message = open("encrypted_memory.txt", "r").read()
enc = []
idx = 0
while idx < len(message):
    temp = ""
    if message[idx] == "'":
        idx += 1
        while True:
            if message[idx] == "'":
                break
            temp += message[idx]
            idx += 1
    if temp != '':
        enc.append(temp)
    idx += 1
print(enc)

decrypt = ""
for curr in tqdm(enc):
    for char in string.printable:
        x = (ord(char) + 20) % 130
        x = hashlib.sha512(str(x).encode()).hexdigest()
        for method in methods:
            y = encrypt(x,method)
            if y == curr:
                decrypt += char

print(decrypt)
