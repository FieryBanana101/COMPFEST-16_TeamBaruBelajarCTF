# [500 pts] Color Palette
### Category: Forensic

**Deskripsi:**
> The visual design team already brainstormed the theme for the Colorfest event, which is "dominance in art". But they are still discussing to choose 5 colors to put into their color palette, can you help them?  
>  
> Flag : COMPFEST16{flag}  
>   
> Author: kilometer

**[coming_soon_colorfest.png](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Color%20Palette/coming_soon_colorfest.png):**

![color.png](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Color%20Palette/coming_soon_colorfest.png)

### Solusi:

Awalnya dicurigai terdapat file tersembunyi di dalam gambar. Namun setelah mencoba "binwalk", "zsteg", dan "steghide" tidak terlihat ada file atau data tersembunyi di dalam file gambar.

Setelah menginspeksi gambar dengan "xxd" atau "hexdump" juga tidak memberikan hasil apa-apa.

Jika kita cermati judul dari soal, "color palette" mengacu pada set warna yang digunakan pada suatu gambar tertentu. 

Jika kita perhatikan, terlihat bahwa gambar tersebut hanya menggunakan 6 warna yang berbeda.

Untuk itu, mari kita ambil nilai hex dari setiap warna yang muncul menggunakan [online color picker](https://redketchup.io/color-picker), didapatkan warna:
```
#FFFFFF : putih
#B6BBB7 : abu-abu
#734974 : ungu tua
#AEC8A7 : hijau
#B35777 : merah muda
#CB4BAE : ungu-merah muda
```
**Note:** terurut berdasarkan banyaknya warna pada gambar (dari paling banyak hingga paling sedikit)

Setelah mencoba-coba, jika nilai hex tersebut kita satukan dan diubah menjadi sebuah string panjang dan diubah menjadi base64 menggunakan [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')To_Base64('A-Za-z0-9%2B/%3D')&input=QjZCQkI3DQo3MzQ5NzQNCkFFQzhBNw0KQjM1Nzc3DQpDQjRCQUUNCg&ieol=CRLF&oeol=NEL), didapatkan:
```
////tru3c0l0rsins1d3y0uu
```
**Note:** gunakan opsi 'From Hex' dan 'To Base64' pada CyberChef.

Menurut ketentuan, flag hanya mengandung karakter alphanumeric (\w+) atau karakter '_', sehingga karakter '/' kemungkinan besar bukan bagian dari flag.

Langkah terakhir yang perlu dilakukan yaitu, hilangkan karakter '/' dan wrap dengan "COMPFEST16{}", flag telah didapatkan.

> Flag: **COMPFEST16{tru3c0l0rsins1d3y0uu}**
