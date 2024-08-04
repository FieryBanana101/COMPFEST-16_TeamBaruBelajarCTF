# [500 pts] Industrialspy2
**Deskripsi:**
>After we intercepted Lyubov's last attempt at stealing documents, she disabled our RAM capturer. Fortunately, we still have other loggers active. Is she still trying?
>
>Author: k3ng

Diberikan sebuah file packet capture _traffic.pcapng_, setelah dibuka menggunakan tshark dengan command:
>tshark -r traffic.pcapng -V

Didapatkan USB packet capture antara _host_ dan _2.28.1_, dalam beberapa frame terdapat HID data yang saya curigai berisi petunjuk flag, supaya lebih jelas dibuka kembali dengan command:
>tshark -r traffic.pcapng -V | grep "HID Data:"

output:
>HID Data: 0000060000000000  
HID Data: 0000000000000000  
HID Data: 00000b0000000000  
HID Data: 0000000000000000  
HID Data: 0000150000000000  
HID Data: 0000000000000000  
HID Data: 0000120000000000  
...

HID atau Human Interface Data ini kemungkinan besar berasal dari input keyboard yang disimpan dalam hex sesuai USB codes. Setelah mencari di internet, ditemukan script decoder yang ditulis yang bisa mengubah usb codes dari leftover data menjadi karakter ascii: [script by natesinger](https://github.com/natesinger/KeyBD-PCAP-Decoder/blob/main/decode.py).

Karena kita butuh meng-decode HID data, maka perlu dilakukan beberapa modifikasi pada script tersebut sehingga akhirnya didapatkan [script solver](https://github.com/FieryBanana101/COMPFEST16_TeamBaruBelajarCTF/blob/main/Hacker%20Class/Industrialspy2/Industrialspy2.py) yang bisa menemukan flag.

Terakhir, run script tersebut dengan command:
>./Industrialspy2.py ./traffic.pcapng

(Note: jangan lupa untuk memberi execute permission pada script solver sebelum di run)  

Dan akan didapatkan flag.

>Flag: COMPFEST16{L0Ve_m3_s0me_USB_f0rens1CS_fd746ec8b3}

