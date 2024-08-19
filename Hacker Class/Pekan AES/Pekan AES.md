# [500 pts] Pekan AES
### Category: Cryptography

**Deskripsi:**
>ECB mode is secure right?  
>  
>Author: swusjask  
>  
>nc challenges.ctf.compfest.id 20015  

**chall.py:**
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 16))

def decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 16)

def menu():
    print("1. Encrypt Message")
    print("2. Get Flag")
    print("3. Exit")
    choice = int(input(">> "))
    return choice

key = os.urandom(16)

while True:
    choice = menu()
    if choice == 1:
        plaintext = input("Message: ")
        if 'COMPFEST16' in plaintext:
            print("Nope.")
            continue
        print("Encrypted Message (hex):", encrypt(key, plaintext.encode()).hex())
    elif choice == 2:
        ciphertext = input("Encrypted Message (hex): ")
        try:
            plaintext = decrypt(key, bytes.fromhex(ciphertext)).decode()
            if 'COMPFEST16' in plaintext:
                print(open('flag.txt').read())
        except:
            print("Invalid ciphertext.")
    elif choice == 3:
        break
```

### Solusi
Diberikan sebuah oracle yang dapat melakukan enkripsi AES-ECB pada string input, kecuali jika string input memiliki substring "COMPFEST16".

Kita juga dapat mendapatkan flag pada oracle tersebut melalui opsi 2, yang akan meminta input berupa ciphertext AES-ECB. 

Flag hanya akan didapat jika ciphertext yang di-input menghasilkan plaintext yang memiliki substring "COMPFEST16". Maka tujuan kita yaitu mencari ciphertext dari plaintext yang memiliki substring "COMPFEST16".

Karena mode yang digunakan AES pada program yaitu [ECB](https://www.youtube.com/watch?v=jDnenb9EHQk), maka kita dapat meng-bypass larangan input substring "COMPFEST16" dengan cara memisah substring menjadi 2 substring berbeda kemudian kita satukan kembali ciphertext-nya.

Dari source code terlihat bahwa block size pada ECB yaitu 16, maka didapatkan properti berikut yang bisa dimanfaatkan:
```python
encrypt('a' * 16 + 'b' * 16) = encrypt('a' * 16) + encrypt('b' * 16)
```

Cara kita memanfaatkannya yaitu, kita bisa membagi "COMPFEST16" menjadi "COMPFEST1" dan "6" dan kita cari ciphertext masing-masing sehingga bisa meng-bypass filter.

Misalnya dapat kita gunakan:
> Substring 1: "a" * 7 + "COMPFEST1" (16 karakter)  
> Substring 2: "6" + "a" * 15 (16 karakter)  
> Ciphertext : encrpyt(Substring 1) + encrypt(Substring 2)
>   
> **Note: "a" hanya digunakan untuk padding agar panjang substring tepat 16 karakter**

Kombinasi tersebut dapat digunakan, karena:
```python
encrypt("a"*7 + "COMPFEST1") + encrypt("6" + "a" * 15)
= encrypt("a" * 7 + "COMPFEST1" + "6" + "a" * 15)
= encrypt("a" * 7 + "COMPFEST16" + "a" * 15)  # ----------------> Terdapat substring yang dibutuhkan untuk mengambil flag
```

Setelah mendapatkan ciphertext yang tepat, masih ada langkah tambahan.

Karena algoritma pad() yang digunakan pada source code tetap meng-pad plaintext walaupun panjangnya sudah tepat 16 karakter, maka ciphertext juga harus ditambah dengan hasil encrypt(random_pad_character * 16) agar hasil ciphertext dinyatakan valid.

Sehingga hasil ciphertext yang dapat digunakan untuk mengambil flag pada opsi 2 yaitu:
```python
ciphertext = encrypt("a" * 7 + "COMPFEST1") + encrypt("6" + "a" * 15) + encrypt(random_pad_character * 16)
```
**Note 1:** hasil dari encrypt() diambil setengah saja, karena setengah selanjutnya berasal dari padding di plaintext.

**Note 2:** random_pad_character harus karakter non-printable (misal \x01) agar bisa di unpad dengan benar pada decrypt().

Solver script: [Pekan AES.py](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Pekan%20AES/Pekan%20AES.py)

> Flag: **COMPFEST16{ECB_kurang_bagus_untuk_dipake_bro_gak_jaman_61abdb8843}**
