# [500 pts] small secret
### Category: Cryptography

**Deksripsi:**  
Hmmm....., There's something fishy about the secret key

Author: swusjask

**chall.py:**
```python
from Crypto.Util.number import *
from Crypto.Util.Padding import pad

p = getPrime(256)
q = getPrime(256)
n = p * q

while True:
    d = getPrime(128)
    if GCD(d, (p - 1) * (q - 1)) == 1:
        e = inverse(d, (p - 1) * (q - 1))
        break

flag = b"COMPFEST16{REDACTED}"

m = bytes_to_long(pad(flag, n.bit_length() // 8))
c = pow(m, e, n)
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}" 
```
**chall.txt:**
```
n = 4343181431018200306551934767651740434698197697113054708645833834136507352526415886520288547842511292184443469018500774366124208475728287550710509139311991
e = 990392646460034135448171148543952400451416256633912637496937644405710261537403000592902653902423256951347857173056999413638412612185130835028620999928903
c = 79203839707597357456095115220720812537064056637017832867021677647242116974855711501919695341014184758746900399710417605865392358809039924384193670071524
```

### Solusi

Script chall.py melakukan generasi public key dan private key RSA secara tidak benar. Script melakukan generasi private key terlebih dahulu, kemudian membuat public key dengan mencari inverse private key.

Cara generasi key tersebut berbahaya karena nilai private key (d) yang dihasilkan akan sangat kecil jika dibandingkan dengan nilai public key (n, e), dan ciphertext (c).

Nilai d yang kecil dapat diserang menggunakan [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack).

Untuk mempermudah implementasi wiener's attack, dapat digunakan online tools yang tersedia seperti: https://www.dcode.fr/rsa-cipher

Masukkan nilai public key dan ciphertext, dan pilih opsi "Plaintext as Character String", kemudian flag akan didapatkan:
![RSA Decoder](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-19%20142624.png)

> Flag: **COMPFEST16{jUzT_sMaLl_S3cReT_bEtWe3n_uS_ed2c699bb3}**
