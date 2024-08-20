# Evil Jarkom
### Category: Forensic

**Deskripsi:**
> i am currently taking jarkom this semester and working on an assignment but the capture result is weird, a lot of random characters.
> 
> Author: k3ng

**Attachment:** [traffic.pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Evil%20Jarkom/traffic.pcapng)

### Solusi

Setelah membuka file .pcapng dengan wireshark, didapatkan banyak packet dengan 2 tcp stream. 

![traffic.pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-20%20192702.png)

Setelah lama memperhatikan packet-packet secara random, hal mencurigakan yang terlihat yaitu terdapat packet dengan IPv4 header yang memiliki "Reserved Bit" pada "Flags" yang bernilai 1 (dapat dilihat pada bagian kiri bawah).

![traffic.pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-20%20192824.png)

Informasi lebih lanjut: https://www.ipxo.com/blog/ipv4-packet-header/

Menurut referensi dari internet, bagian "Flags" pada IPv4 header memiliki 3 bit : '000'

Bit kedua dan ketiga mengandung informasi terkait apakah packet ter-fragmented. Sedangkan bit pertama ter-reserved dan selalu bernilai 0. Disini bit pertama bernilai 1 sehingga sangat mencurigakan.

Dengan menggunakan filter wireshark 'ip.flags.rb == 1' kita dapat melihat seluruh packet dengan reserved bit yang bernilai 1.

![traffic.pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-20%20192901.png)

Terlihat bahwa seluruh packet tersebut berisi content data berupa 1 ascii karakter untuk setiap packet (dapat dilihat pada bagian kanan bawah, terdapat karakter 'C' yang merupakan data dari packet).

> Packet pertama berisi karakter 'C'  
> Packet kedua berisi karakter 'O'  
> Packet ketiga berisi karakter 'M'  
> ....  

Terlihat jelas bahwa jika diurutkan, karakter yang muncul akan membentuk string "COMPFEST16{...", sehingga akan didapat flag dari challenge dengan cara mengambil karakter satu per satu secara manual dari packet yang telah difilter.


> Flag: **COMPFEST16{rfc_3514_security_bit_145eef449d}**

**Note:** nama challenge ini merupakan reference pada 'evil bit' dari RFC (https://en.wikipedia.org/wiki/Evil_bit)
