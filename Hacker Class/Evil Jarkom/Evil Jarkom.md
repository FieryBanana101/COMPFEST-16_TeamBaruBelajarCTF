# Evil Jarkom
### Category: Forensic

**Deskripsi:**
> i am currently taking jarkom this semester and working on an assignment but the capture result is weird, a lot of random characters.
> 
> Author: k3ng

**Attachment:** [traffic.pcapng]()

### Solusi

Setelah membuka file .pcapng dengan wireshark, didapatkan banyak packet dengan 2 tcp stream. 
(gambar)

Setelah lama memperhatikan packet-packet secara random, hal mencurigakan yang terlihat yaitu terdapat packet dengan IPv4 header yang memiliki reserved bit pada flag yang bernilai 1.
(gambar)

Informasi lebih lanjut: https://www.ipxo.com/blog/ipv4-packet-header/

Menurut referensi dari search engine, bagian flag pada IPv4 header memiliki 3 bit : '000'

Bit kedua dan ketiga mengandung informasi terkait apakah packet ter-fragmented. Sedangkan bit pertama ter-reserved dan selalu bernilai 0. Disini bit pertama bernilai 1 sehingga sangat mencurigakan.

Dengan menggunakan filter wireshark 'ip.flags.rb == 1' kita dapat melihat seluruh packet dengan reserved bit yang bernilai 1.
(gambar)

Terlihat bahwa seluruh packet tersebut berisi content data berupa 1 ascii karakter untuk setiap packet.
(gambar)
> Packet pertama berisi karakter 'C'
> Packet kedua berisi karakter 'O'
> packet ketiga berisi karakter 'M'
> ....

Terlihat jelas bahwa jika diurutkan, karakter yang muncul akan membentuk string "COMPFEST16{...", sehingga akan didapat flag dari challenge dengan mengambil karakter satu per satu secara manual dari packet yang telah difilter.

> Flag: **COMPFEST16{rfc_3514_security_bit_145eef449d}**

**Note:** nama challenge ini merupakan reference pada 'evil bit' dari RFC (https://en.wikipedia.org/wiki/Evil_bit)
