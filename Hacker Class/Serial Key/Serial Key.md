# [500 pts] Serial Key
### Category: Reverse Engineering

***Deskripsi***
>Classic reverse, classic serial key
>
>Author: Zanark
>
>nc challenges.ctf.compfest.id 20012
____________________________________________________________________________

Awalnya saya mencoba connect menggunakan netcat pada host dan port yang diberikan,
> Serial 1 ==>

Saya mencoba untuk input beberapa string, namun terus mendapat output "salah".

Diberikan sebuah file tanpa extensi yang dapat kita dissassemble menggunakan decompiler. Agar mudah, saya menggunakan [dogbolt](https://dogbolt.org/?id=2a023dcd-9c76-414f-9a92-a6c1a37583fa#angr=355) dan kita ambil hasil decompile dari _angr_.

Dari hasil decompile, kita hanya perlu melihat fungsi main() dan fungsi check():
```c
  int main(unsigned long a0, unsigned long a1)
{
    unsigned long v0;  // [bp-0xb8]
    unsigned int v1;  // [bp-0xac]
    unsigned int v2;  // [bp-0xa4]
    FILE_t *v3;  // [bp-0xa0]
    char v4[14];  // [bp-0x98]
    char v5;  // [bp-0x78]

    v1 = a0;
    v0 = a1;
    setvbuf(stdout@GLIBC_2.2.5, NULL, 2, 0);
    v2 = 0;
    while (true)
    {
        if (v2 <= 99)
        {
            printf("Serial %d ==> ", v2 + 1);
            __isoc99_scanf("%s", (unsigned int)v4);
            if (!check(v4))
            {
                puts("Salah");
                return 0;
            }
            v2 += 1;
        }
        else
        {
            v3 = &fopen("flag.txt", "r")->_flags;
            __isoc99_fscanf(v3, "%s", (unsigned int)&v5);
            printf("%s", (unsigned int)&v5);
            return 0;
        }
    }
}
```
Secara sederhana, fungsi main() akan mengambil input string selama 100 kali dan input akan di masukkan pada fungsi check(). Jika fungsi check() selalu mengeluarkan nilai True selama 100 kali, maka akan didapatkan flag.

```c
int check(char a0[14])
{
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]
    unsigned int v3;  // [bp-0x64]
    unsigned int v4;  // [bp-0x60]
    unsigned int v5;  // [bp-0x5c]
    char *v6;  // [bp-0x58]
    char v7;  // [bp-0x24]
    char v8;  // [bp-0x23]
    char v9;  // [bp-0x22]
    char v10;  // [bp-0x21]

    if (strlen(a0) != 24)
        return 0;
    for (v0 = 4; v0 <= 23; v0 += 5)
    {
        if (a0[v0] != 45)
            return 0;
    }
    if (a0[10] != 67)
    {
        return 0;
    }
    else if (a0[11] != 70)
    {
        return 0;
    }
    else if (a0[12] != 49)
    {
        return 0;
    }
    else if (a0[13] != 54)
    {
        return 0;
    }
    else
    {
        for (v1 = 0; v1 < idx; v1 += 1)
        {
            if (!strncmp(serial[v1], a0, 24))
                return 0;
        }
        for (v2 = 0; v2 <= 23; v2 += 5)
        {
            for (v3 = v2; v3 <= v2 + 3; v3 += 1)
            {
                v5 = a0[v3];
                if ((v5 <= 47 || v5 > 57) && (!(v5 > 64) || !(v5 <= 90)))
                    return 0;
            }
            v7 = a0[v2];
            v8 = a0[1 + v2];
            v9 = a0[2 + v2];
            v10 = a0[3 + v2];
            for (v4 = 0; v4 < (unsigned int)(v2 / 5); v4 += 1)
            {
                if (!strncmp((&v6)[v4], &v7, 4))
                    return 0;
            }
            (&v6)[v2 / 5] = malloc(4);
            (&v6)[v2 / 5] = strdup(&v7);
        }
        serial[idx] = malloc(24);
        serial[idx] = strdup(a0);
        idx = idx + 1;
        return 1;
    }
}
```
Secara sederhana, fungsi check() akan mengeluarkan nilai True jika argumen string:
1. Memiliki panjang 24
2. string[10]...string[13] == "CF16"
3. string[4], string[9], ... , string[19] == "-"
4. string[0], string[5], ... , string[20] saling berbeda
5. setiap argumen string yang dimasukkan ke fungsi check() pada iterasi di main() selalu berbeda

Sehingga kita tinggal melakukan input string dengan pola:
>A000-B000-CF16-D000-E000  
>A000-B000-CF16-D000-E001  
>A000-B000-CF16-D000-E002  
>...  
>A000-B000-CF16-D000-E100  

Supaya mudah, hal tersebut dapat dilakukan melalui [solver script](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Serial%20Key/Serial%20Key.py).

> Flag: **COMPFEST16{v3rY_st4nd4Rd_k3ygEn_3794611e09}**
