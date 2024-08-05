# [500 pts] Random
### Category: Reverse Engineering

**Deskripsi:**
>With this random, I could create a script to mess up everything.  
>Author: Zanark
____________________________________________________________________

**script.py:**
```python
import random

flag = "" # REDACTED

random.seed(int(flag[8:10]))
for c in flag[:8]:
    random.seed(random.randint(1, 0xCF) + ord(c))

destroyed = ""

for char in flag:
    offset = random.randint(1, 10)
    MyFriend = random.randint(1, 127)
    result = (ord(char) - offset) ^ MyFriend

    if random.randint(0, 1):
        result += 0x16
    
    destroyed += chr(result)

print(destroyed.encode("utf-8"))
# b'!vP3\xc2\x91\xc2\x89\x11\x1f\x06C\x17_\x19t)\xc2\x929\x06li\x1d\x1f\xc2\x88*\x19E+4E\x16\x07v1S$\x1a c\x1flcr4> 3vlt\xc2\x85Yj-$0 '

```
### **Solusi:**

Secara sederhana program tersebut meng-encrypt flag dengan mengubah karakter flag[i] menjadi:
>( flag[i] - random_int(1,10) ) ^ random_int(1,127) + 22 * random_int(0,1)

Perhatikan bahwa dilakukan inisialisasi seed untuk fungsi random, jika kita mengetahui seed dari fungsi random maka program dapat kita reverse engineer untuk mendapatkan flag.

Hal ini karena seed pada fungsi random() akan mengakibatkan urutan dari angka random yang muncul selalu sama, misalnya:
```python
import random
random.seed(123)
print(random.randint(1,100))
print(random.randint(2,5))
print(random.random())
```
**Output:**
>7  
>4  
>0.08718667752263232  

Output akan selalu sama urutannya setiap program dijalankan hal ini terjadi karena inisialisasi seed 123 pada random(). Informasi lebih lanjut: https://www.w3schools.com/python/ref_random_seed.asp

Maka dapat kita bruteforce seed yang digunakan dan kita lakukan inverse pada operasi yang meng-encrypt flag tersebut menggunakan angka random dari setiap seed.
Dapat dilihat di source code, kemungkinan seed yang digunakan adalah: 
>random_integer(1, 0xCF) + ord(c)  
>0xCF = 207 dalam bentuk hexadecimal  
>ord(c) = kode ascii dari karakter di flag

Untuk mengetahui range yang perlu di bruteforce, kita lihat kemungkinan terbesar dari nilai random_interger(1, 207) + ord(c)
> Nilai ord(c) terbesar yaitu 126 (didapat dari karakter printable dengan nilai ascii terbesar)

Sehingga kemungkinan terbesar yaitu 207 + 126 = 333. Maka tinggal kita bruteforce untuk setiap seed dari 1 hingga 333 dan lakukan inverse
pada setiap operasi yang dilakukan, akhirnya akan didapatkan flag.

Implementasi: [script solver](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Random/Random.py)

>Flag: **COMPFEST16{C0mpu73r_c0uld_n0t_m4k3_Tru3_R4nd_0be49a7429}**
