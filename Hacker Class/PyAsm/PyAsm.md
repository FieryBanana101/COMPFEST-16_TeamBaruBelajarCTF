# [500 pts] PyAsm
### Category: Reverse Engineering

**Deskripsi:**
>Python but assembly. What??  
>  
>Author: Zanark  
>  
>nc challenges.ctf.compfest.id 20011

**chall:**
```python
  0           0 RESUME                   0

  1           2 PUSH_NULL
              4 LOAD_NAME                0 (input)
              6 LOAD_CONST               0 ('Enter THE password: ')
              8 PRECALL                  1
             12 CALL                     1
             22 STORE_NAME               1 (pw)

  3          24 LOAD_NAME                1 (pw)
             26 LOAD_METHOD              2 (isalnum)
             48 PRECALL                  0
             52 CALL                     0
             62 POP_JUMP_FORWARD_IF_TRUE    21 (to 106)

  4          64 PUSH_NULL
             66 LOAD_NAME                3 (print)
             68 LOAD_CONST               1 ('Password format is not valid!')
             70 PRECALL                  1
             74 CALL                     1
             84 POP_TOP

  5          86 PUSH_NULL
             88 LOAD_NAME                4 (exit)
             90 PRECALL                  0
             94 CALL                     0
            104 POP_TOP

  7     >>  106 PUSH_NULL
            108 LOAD_NAME                5 (len)
            110 LOAD_NAME                1 (pw)
            112 PRECALL                  1
            116 CALL                     1
            126 LOAD_CONST               2 (9)
            128 COMPARE_OP               4 (>)
            134 POP_JUMP_FORWARD_IF_FALSE    21 (to 178)

  8         136 PUSH_NULL
            138 LOAD_NAME                3 (print)
            140 LOAD_CONST               3 ('Password is too long!')
            142 PRECALL                  1
            146 CALL                     1
            156 POP_TOP

  9         158 PUSH_NULL
            160 LOAD_NAME                4 (exit)
            162 PRECALL                  0
            166 CALL                     0
            176 POP_TOP

 11     >>  178 PUSH_NULL
            180 LOAD_NAME                5 (len)
            182 LOAD_NAME                1 (pw)
            184 PRECALL                  1
            188 CALL                     1
            198 LOAD_CONST               2 (9)
            200 COMPARE_OP               0 (<)
            206 POP_JUMP_FORWARD_IF_FALSE    21 (to 250)

 12         208 PUSH_NULL
            210 LOAD_NAME                3 (print)
            212 LOAD_CONST               4 ('Password is too short!')
            214 PRECALL                  1
            218 CALL                     1
            228 POP_TOP

 13         230 PUSH_NULL
            232 LOAD_NAME                4 (exit)
            234 PRECALL                  0
            238 CALL                     0
            248 POP_TOP

 15     >>  250 BUILD_LIST               0
            252 LOAD_CONST               5 ((0, 0, 0, 0, 0, 0, 0, 0, 0))
            254 LIST_EXTEND              1
            256 STORE_NAME               6 (x)

 16         258 PUSH_NULL
            260 LOAD_NAME                7 (range)
            262 LOAD_CONST               2 (9)
            264 PRECALL                  1
            268 CALL                     1
            278 GET_ITER
        >>  280 FOR_ITER                37 (to 356)
            282 STORE_NAME               8 (i)

 17         284 PUSH_NULL
            286 LOAD_NAME                9 (ord)
            288 LOAD_NAME                1 (pw)
            290 LOAD_NAME                8 (i)
            292 BINARY_SUBSCR
            302 PRECALL                  1
            306 CALL                     1
            316 LOAD_NAME                6 (x)
            318 PUSH_NULL
            320 LOAD_NAME                5 (len)
            322 LOAD_NAME                6 (x)
            324 PRECALL                  1
            328 CALL                     1
            338 LOAD_NAME                8 (i)
            340 BINARY_OP               10 (-)
            344 LOAD_CONST               6 (1)
            346 BINARY_OP               10 (-)
            350 STORE_SUBSCR
            354 JUMP_BACKWARD           38 (to 280)

 19     >>  356 PUSH_NULL
            358 LOAD_NAME                3 (print)
            360 LOAD_NAME                6 (x)
            362 PRECALL                  1
            366 CALL                     1
            376 POP_TOP

 21         378 LOAD_NAME                6 (x)
            380 LOAD_CONST               7 (7)
            382 BINARY_SUBSCR
            392 LOAD_CONST               8 (69)
            394 BINARY_OP                0 (+)
            398 LOAD_CONST               9 (120)
            400 COMPARE_OP               2 (==)
            406 POP_JUMP_FORWARD_IF_FALSE   174 (to 756)

 22         408 LOAD_NAME                6 (x)
            410 LOAD_CONST              10 (3)
            412 BINARY_SUBSCR
            422 LOAD_CONST              11 (1337)
            424 BINARY_OP               12 (^)
            428 LOAD_CONST              12 (1355)
            430 COMPARE_OP               2 (==)
            436 POP_JUMP_FORWARD_IF_FALSE   159 (to 756)

 23         438 LOAD_NAME                6 (x)
            440 LOAD_CONST              13 (0)
            442 BINARY_SUBSCR
            452 LOAD_CONST              14 (22)
            454 BINARY_OP                2 (//)
            458 LOAD_CONST              15 (5)
            460 COMPARE_OP               2 (==)
            466 POP_JUMP_FORWARD_IF_FALSE   144 (to 756)

 24         468 LOAD_NAME                6 (x)
            470 LOAD_CONST              16 (4)
            472 BINARY_SUBSCR
            482 LOAD_CONST              17 (16)
            484 BINARY_OP               10 (-)
            488 LOAD_CONST              18 (35)
            490 COMPARE_OP               2 (==)
            496 POP_JUMP_FORWARD_IF_FALSE   129 (to 756)

 25         498 LOAD_NAME                6 (x)
            500 LOAD_CONST              19 (8)
            502 BINARY_SUBSCR
            512 LOAD_CONST              10 (3)
            514 BINARY_OP                3 (<<)
            518 LOAD_CONST              20 (832)
            520 COMPARE_OP               2 (==)
            526 POP_JUMP_FORWARD_IF_FALSE   114 (to 756)

 26         528 LOAD_NAME                6 (x)
            530 LOAD_CONST               6 (1)
            532 BINARY_SUBSCR
            542 LOAD_CONST              21 (2)
            544 BINARY_OP                8 (**)
            548 LOAD_CONST              22 (9409)
            550 COMPARE_OP               2 (==)
            556 POP_JUMP_FORWARD_IF_FALSE    99 (to 756)

 27         558 LOAD_NAME                6 (x)
            560 LOAD_CONST              23 (6)
            562 BINARY_SUBSCR
            572 LOAD_CONST               7 (7)
            574 BINARY_OP                5 (*)
            578 LOAD_CONST              24 (693)
            580 COMPARE_OP               2 (==)
            586 POP_JUMP_FORWARD_IF_FALSE    84 (to 756)

 28         588 LOAD_NAME                6 (x)
            590 LOAD_CONST              21 (2)
            592 BINARY_SUBSCR
            602 UNARY_INVERT
            604 LOAD_CONST              25 (-110)
            606 COMPARE_OP               2 (==)
            612 POP_JUMP_FORWARD_IF_FALSE    71 (to 756)

 29         614 LOAD_NAME                6 (x)
            616 LOAD_CONST              15 (5)
            618 BINARY_SUBSCR
            628 LOAD_CONST              26 (107)
            630 COMPARE_OP               2 (==)
            636 POP_JUMP_FORWARD_IF_FALSE    59 (to 756)

 30         638 PUSH_NULL
            640 LOAD_NAME                3 (print)
            642 LOAD_CONST              27 ("Correct! Here's your flag: ")
            644 PRECALL                  1
            648 CALL                     1
            658 POP_TOP

 31         660 PUSH_NULL
            662 LOAD_NAME                3 (print)
            664 PUSH_NULL
            666 LOAD_NAME               10 (open)
            668 LOAD_CONST              28 ('flag.txt')
            670 PRECALL                  1
            674 CALL                     1
            684 LOAD_METHOD             11 (read)
            706 PRECALL                  0
            710 CALL                     0
            720 PRECALL                  1
            724 CALL                     1
            734 POP_TOP

 32         736 PUSH_NULL
            738 LOAD_NAME                4 (exit)
            740 PRECALL                  0
            744 CALL                     0
            754 POP_TOP

 34     >>  756 PUSH_NULL
            758 LOAD_NAME                3 (print)
            760 LOAD_CONST              29 ('Wrong password.')
            762 PRECALL                  1
            766 CALL                     1
            776 POP_TOP
            778 LOAD_CONST              30 (None)
            780 RETURN_VALUE

```

### Solusi:

Diberikan file attachment berupa python bytecode (hasil compile dari file .py). Namun hasil compile diberikan dalam bentuk file .txt bukan .pyc sehingga akan sulit untuk di decompile.

Namun kita tidak perlu melakukan decompile karena file yang diberikan cukup pendek, sehingga dapat kita decompile secara manual.

Awalnya coba dulu jalankan program pada server challenge:
```
nc challenge.ctf.compfest.id 20011
```

Output:
```
Enter THE password:
```

Program meminta kita untuk memasukkan password. Setelah mencoba memasukkan string "a", didapatkan output "Password is too short!".

Sedangkan setelah mencoba memasukkan string "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", didapatkan output "Password is too long!".

Setelah mencoba beberapa string dengan panjang berbeda lainnya, didapatkan output "Wrong password" pada input string "aaaaaaaaa" (9 karakter).

Artinya panjang password yang harus dimasukkan yaitu 9 karakter.

Kemudian mari kita coba perhatikan beberapa hasil decompile source code:
```python
 15     >>  250 BUILD_LIST               0
            252 LOAD_CONST               5 ((0, 0, 0, 0, 0, 0, 0, 0, 0))
            254 LIST_EXTEND              1
            256 STORE_NAME               6 (x)
```

Pada instruksi 15, program membuat variabel x dengan type list dan diinisialisasi sebagai [0,0,0,0,0,0,0,0,0]

```python
 16         258 PUSH_NULL
            260 LOAD_NAME                7 (range)
            262 LOAD_CONST               2 (9)
            264 PRECALL                  1
            268 CALL                     1
            278 GET_ITER
        >>  280 FOR_ITER                37 (to 356)
            282 STORE_NAME               8 (i)

 17         284 PUSH_NULL
            286 LOAD_NAME                9 (ord)
            288 LOAD_NAME                1 (pw)
            290 LOAD_NAME                8 (i)
            292 BINARY_SUBSCR
            302 PRECALL                  1
            306 CALL                     1
            316 LOAD_NAME                6 (x)
            318 PUSH_NULL
            320 LOAD_NAME                5 (len)
            322 LOAD_NAME                6 (x)
            324 PRECALL                  1
            328 CALL                     1
            338 LOAD_NAME                8 (i)
            340 BINARY_OP               10 (-)
            344 LOAD_CONST               6 (1)
            346 BINARY_OP               10 (-)
            350 STORE_SUBSCR
            354 JUMP_BACKWARD           38 (to 280)
```
Pada instruksi 16-17 dilakukan modifikasi terhadap variabel x, yang dilakukan oleh program yaitu dapat digambarkan sebagai berikut (pw = password) :
```python
for i in range(9,-1,-1):
    x[i] = ord(pw[9-i])
```

Secara sederhana x akan diisi dengan kode ascii karakter dari password, kemudian akan di reverse.

Setelahnya akan dilakukan pengecekan pada elemen list x, pengecekan ini akan menentukan apakah password benar atau salah.
```python
 21         378 LOAD_NAME                6 (x)
            380 LOAD_CONST               7 (7)
            382 BINARY_SUBSCR
            392 LOAD_CONST               8 (69)
            394 BINARY_OP                0 (+)
            398 LOAD_CONST               9 (120)
            400 COMPARE_OP               2 (==)
            406 POP_JUMP_FORWARD_IF_FALSE   174 (to 756)
```
Pada instruksi 21, dilakukan pengecekan dengan compare operator '==', jika pengecekan menghasilkan "False" maka program akan "jump" ke line 756:
```python
 34     >>  756 PUSH_NULL
            758 LOAD_NAME                3 (print)
            760 LOAD_CONST              29 ('Wrong password.')
            762 PRECALL                  1
            766 CALL                     1
            776 POP_TOP
            778 LOAD_CONST              30 (None)
            780 RETURN_VALUE
```
Yang artinya, program akan meng-output "Wrong password", kemudian exit dari program dengan return value "None".

Sehingga pengecekan pada instruksi 21 setara dengan:
```python
if x[7] + 69 != 120:
    print('Wrong password.')
    return None
```
Dari sini dapat disimpulkan bahwa x[7] = 120 + 69, sehingga berhasil kita dapatkan salah satu elemen x.

Hal yang sama kemudian dapat dilakukan pada instruksi 22-29 untuk menemukan nilai elemen-elemen x lainnya. Didapatkan:
```python
x[7] + 69 = 120
x[3] ^ 1337 = 1355
x[0] // 22 = 5
x[4] - 16 = 35
x[8] << 3 = 832
x[1] ** 2 = 9409
x[6] * 7 = 693
~x[2] = -110
x[5] = 107
```
Sehingga dapat ditemukan semua elemen-elemen x, yaitu:
```python
x[7] = 120-69
x[3] = 1337 ^ 1355
x[0] = 5 * 22
x[4] = 16+35
x[8] = 832 // 8
x[1] = floor(sqrt(9409))
x[6] = 693 // 7
x[2] = ~(-110)
x[5] = 107
```
Setelah x ditemukan, reverse list x untuk mendapatkan kode ascii dari password. Password pun ditemukan (implementasi pada solver script dibawah).

> **Note:**  
> '^' adalah binary operator xor  
> '<<' adalah binary operator shift left  
> '~' adalah unary operator invert  
> Informasi lebih lanjut dapat dicari melalui search engine

Solver script: [PyAsm.py]()

> Flag: **COMPFEST16{pYth0n_4sm_1s_3z_r1gtH?_6b6241e4c8}**

