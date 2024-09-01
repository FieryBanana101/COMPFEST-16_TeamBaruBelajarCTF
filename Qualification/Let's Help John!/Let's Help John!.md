# Let's Help John!
### Category: Web Exploitation

**Deskripsi:**
```
Oh no! My ex-cellmate got jailed again! Help me leave a key for him!

Author: Ultramy

http://challenges.ctf.compfest.id:9016
```
### Solusi:

Dengan membuka link website yang diberikan terlihat index page:

![website](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20155543.png)

Kemudian kita coba meng-klik tombol "play" yang diberikan:

![play](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20155549.png)

Terlihat bahwa kita menemukan jalan buntu dan untuk bisa lanjut kita harus berasal dari website "http://state.com", maka dari itu dapat kita lakukan modifikasi HTTP header untuk bisa lanjut.

Selanjutnya dapat digunakan burpsuite, kita intercept request saat meng-klik play dan masukkan request tersebut ke repeater burpsuite:

![burpsuite](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20155935.png)

Tambahkan header field "Referer: http://state.com", yang akan memberi tahu website bahwa kita meng-klik link ini melalui website "http://state.com" (padahal sebenarnya tidak), response yang didapatkan:

![response](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20155945.png)

Selanjutnya, kita diperlukan untuk mengubah kuantitas cookie yang diperbolehkan dari website menjadi "Unlimited", hal ini dapat kita lakukan dengan menambahkan header field "Cookie: quantity=Unlimited", setelahnya kita cek kembali respon website.

![repeater](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161546.png)

![response](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161553.png)

Dari respon, website hanya memperbolehkan kita mengunjungi nya dengan aplikasi "AgentYessir", hal ini dapat kita atasi dengan memodifikasi HTTP header "User-Agent":

![repeater](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161616.png)

![response](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161624.png)

Kemudian, kita diharuskan memodifikasi field "From" yang berisi kontak dari orang yang menjalankan "User-Agent" untuk mengakses website, yang perlu kita lakukan yaitu hanya menambahkan "From: pinkus@cellmate.com"

![repeater](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161648.png)

![response](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-09-01%20161655.png)

Kemudian akan didaptkan flag dari respon website.

> Flag: **COMPFEST16{nOW_h3Lp_H1m_1n_john-O-jail-misc_8506972ce3}**
