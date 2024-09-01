# Industrialspy 3
### Category: Forensic

**Deskripsi:**
```
Dear X,

I welcome you to the internship program at Collective Inc. Your first task is to figure out what happened to one of our servers. We have a suspicion that someone logged in and did something. We recovered some files to help you figure this out.

If you have figured it out, submit your report to nc challenges.ctf.compfest.id 9009.

Author: k3ng
```
### Solusi:

Dengan melakukan netcat pada host dan port yang diberikan deskripsi, kita diberikan pertanyaan:

![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161859.png)

Buka file .pcapng yang diberikan menggunakan wireshark, akan terlihat komunikasi yang menggunakan protokol TCP antara IP 192.168.56.1 dan 192.168.56.11. 

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20005315.png)

Jika kita cermati, IP 192.168.56.11 Banyak mengirim flags [RST, ACK] yang artinya IP tersebut menerima paket dan memberi respon bahwa "port tertutup", sehingga dapat kita asumsikan IP 192.168.56.11 adalah mesin yang diserang dan IP 192.168.56.1 adalah penyerang.

Untuk melihat port nomor berapa yang terbuka dan tertutup pada mesin yang diserang, kita dapat melihat respon dari IP 192.168.56.11 ketika diberi packet TCP dengan nilai flag [SYN]. Jika respons yang diberikan [RST, ACK] artinya port tertutup, namun jika respons tersebut berisi [SYN, ACK] artinya port terbuka.

Nilai byte [SYN, ACK] pada flag tcp setara dengan bilangan basis 2 "10010" atau basis 10 "18". Maka di dalam wireshark dapat digunakan filter:
```
ip.src == 192.168.56.11 and tcp.flags == 18
```

Akan didapatkan:

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20013050.png)

Terlihat pada bagian info bahwa port yang terbuka hanya port 22 dan 5432.

![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161916.png)

Pertanyaan selanjutnya yaitu apa kredensial (username dan password) yang digunakan oleh penyerang untuk masuk ke database?

Jika kita perhatikan lebih lanjut, selain protokol TCP packet capture juga berisi protokol PGSQL yang digunakan untuk melakukan query ke database SQL (dapat digunakan filter "pgsql" untuk mempermudah pencarian).

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20010231.png)

Pada column info kita bisa lihat tipe dari response yang diberikan. 
```
">?" artinya user memberi kredensial username.
"<R" artinya server meminta autentikasi (password) pada user
">p" artinya user memberi kredensial password
"<E" artinya terjadi error karena autentikasi gagal (password salah)
```

Jika kita lihat, dapat disimpulkan bahwa penyerang banyak melakukan input password yang salah (banyak terjadi response "<E"). Namun pada akhirnya penyerang berhasil login (diketahui berhasil karena server tidak merespons dengan "<E").

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20010832.png)

Dapat disimpulkan bahwa kredensial yang digunakan pada sesi login tersebut (packet 4564-4568) adalah kredensial yang digunakan penyerang. Username (packet 4564) adalah "server" dan Password (packet 4568) adalah "changeme".
![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161935.png)

Pertnyaan selanjutnya adalah apa password dari superuser (administrator) pada server database? Pada packet 4586 ditunjukkan data semua user berupa id, nama asli, username, password, dan email. 

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20011332.png)

Terlihat user "super user" dengan id 0 memiliki password "588831adfca19bb4426334b69d9fb49f873e8a22", namun tentunya password yang disimpan tersebut hanya hasil hash dari password asli. Perlu dilakukan cracking menggunakan [john the ripper](https://www.freecodecamp.org/news/crack-passwords-using-john-the-ripper-pentesting-tutorial/) dan wordlist [rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) untuk mendapat password asli:

![john](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20015111.png)

Didapatkan password dari Superuser yaitu "cafecoagroindustrialdelpacfico".

![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161955.png)

Pertanyaan selanjutnya yaitu tabel apa yang dimodifikasi attacker pada server database?

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20012028.png)

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20012046.png)

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20012105.png)

Terlihat bahwa attacker melakukan query untuk melihat tabel "penalties" dari user dengan id 6 lalu menghapusnya.

![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20162013.png)

Pertanyaan selanjutnya yaitu apa identitas nama asli dari attacker? 

Sebelumnya attacker berusaha menghapus tabel "penalties" untuk user dengan id 6, sehingga bisa diasumsikan bahwa attacker merupakan user dengan id 6. 

![pcapng](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-02%20012738.png)

Dapat dilihat pada packet 4586 bahwa user dengan id 6 memiliki nama asli "Lyubov Pryadko".
![netcat](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20162027.png)

Setalah berhasil menjawab langsung didapatkan flag.

> Flag: **COMPFEST16{h3lla_ez_DF1R_t4sK_f0r_4n_1nt3rN_b96818fd79}**
