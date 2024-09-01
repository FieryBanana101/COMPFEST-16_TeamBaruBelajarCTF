# sigma code
### Category: Miscellaneous

**Deskripsi:**
```
My mewing robot is trying to tell me something

Author: Keego
```

**Attachment: [only_sigmas_will_understand.mp3](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Qualification/sigma%20code/only_sigmas_will_understand.mp3)**
### Solusi:

File .mp3 yang diberikan berisi Text-To-Voice yang membacakan angka-angka desimal dalam bahasa inggris. Berikut angka-angka yang dibacakan:
```
81 48 57 78 85 69 90 70 85 49 81 120 78 110 116 53 78 72
108 102 77 122 86 107 77 68 89 49 77 84 78 107 90 72 48 61
```

Karena curiga angka-angka tersebut merupakan kode ascii, maka mari kita coba masukkan ke [converter](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html):

![converter](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20231938.png)

Terlihat dihasilkan string ascii yang berbentuk base64 (dapat dilihat dari adanya padding karakter "="), sehingga dapat kita masukkan string base64 tersebut pada converter, hasilnya:

![converter](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20232305.png)

Terlihat string ascii yang dihasilkan merupakan flag yang kita cari.

> Flag: **COMPFEST16{y4y_35d06513dd}**

