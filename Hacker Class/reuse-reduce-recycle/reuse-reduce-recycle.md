# [500 pts] reuse reduce recycle
### Category: Cryptoghraphy
**Deskripsi:**  
>I changed the mode to CTR, nothing can go wrong right?  
>
>Author: fahrul  
>
>nc challenges.ctf.compfest.id 20016

Diberikan koneksi ke host challenges.ctf.compfest.id dengan port 20016, diberikan juga attachment berupa source code yang berjalan di koneksi tersebut
>chall.py:
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CTR, nonce=IV)
    return cipher.encrypt(pad(plaintext, 16))

def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_CTR, nonce=IV)
    return unpad(cipher.decrypt(ciphertext), 16)

def menu():
    print("1. Encrypt Message")
    print("2. Get Flag")
    print("3. Exit")
    choice = int(input(">> "))
    return choice


key = os.urandom(16)
IV = os.urandom(8)

while True:
    choice = menu()
    if choice == 1:
        plaintext = input("Message: ")
        print("Encrypted Message (hex):", encrypt(key, plaintext.encode()).hex())
    elif choice == 2:
        print("Encrypted Message (hex):", encrypt(key, b"COMPFEST16{RETACDED}").hex())
    elif choice == 3:
        break
```
Source code melakukan 2 hal:  
1. Memberi hasil enkripsi AES-CTR dari input user dalam bentuk hex
2. Mengberi hasil enkripsi flag challenge

AES-CTR di source code menggunakan nonce yang sama, dan karena AES-CTR adalah block cipher maka antara 2 plaintext berbeda akan memiliki persamaan dalam hasil enkripsi jika terdapat karakter yang sama. Maka, dapat dilakukan bruteforce dengan mencoba seluruh karakter printable dan mengecek apakah hasil enkripsi memliki persamaan dengan prefix hasil enkripsi flag (input akan di padding menjadi sebesar 16 block, tambahan padding tidak perlu di cek kesamaannya).

Solver: [reuse-reduce.recyle.py]()
>Flag: COMPFEST16{IV_Reuse_Is_Dangerous_f48375ef51}
