# [500 pts] Baby Rizztekin
### Category: Web Exploitation

**Deskripsi:**
> This is the rizztekin prototype I built long ago, but meervix rewrote it, hmph! I'm sure this one is better.  
>  
> Author: rorre  
>  
> http://challenges.ctf.compfest.id:20003

**app.py:**
```python
from hashlib import sha256
from flask import Flask, redirect, request, g
import os
import sqlite3

FLAG = "COMPFEST16{FLAG}"
SECRET = os.getenv("SECRET") or "epicsecret"
app = Flask(__name__)


def init():
    db = sqlite3.connect("/tmp/app.db")
    db.execute(
        """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        is_admin INT DEFAULT 0 NOT NULL
        );"""
    )

    # DO NOT SAVE PLAINTEXT PASSWORD IN REAL LIFE!!!!!!!!!!!!!!!!!!
    # Use hashing and salting to save password
    db.execute(
        """INSERT OR IGNORE INTO users(id, username, password, is_admin) VALUES
            (1, 'rorre', 'meow', 0),
            (2, 'meervix', 'toksik', 0);
            """
    )
    db.commit()


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("/tmp/app.db")
    return db


def query(sql: str, params: list[object] | None = None):
    cur = get_db().cursor()
    if not params:
        params = []

    results = []
    for s in sql.split(";"):
        cur.execute(s, params)
        results.append(cur.fetchall())

    get_db().commit()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def create_hash(value: str):
    return sha256((value + SECRET).encode()).hexdigest()


def parse_cookie(value: str):
    try:
        value, hash = value.split("-")
        if create_hash(value) != hash:
            return False, None
        return True, value
    except:
        return False, None


@app.get("/")
def index():
    valid, user = parse_cookie(request.cookies.get("user_id", ""))
    if not valid:
        user = "Guest"

    bottom = "<a href='/login'>Login</a>"
    if user != "Guest":
        row = query("SELECT username, is_admin FROM users WHERE id = ?", [user])[0]
        if row:
            user = row[0][0]
            bottom = "<a href='/logout'>Logout</a>"
            if row[0][1] == 1:
                bottom += f"<p>Flag: {FLAG}</p>"
        else:
            user = "Guest"

    return f"<p>Hello, {user}.</p>{bottom}"


@app.get("/logout")
def logout():
    resp = redirect("/")
    resp.delete_cookie("user_id")
    return resp


@app.get("/login")
def login():
    return """
<form method="POST">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br><br>
    
    <input type="submit" value="Submit">
</form>
"""


@app.post("/login")
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return redirect("/login")

    row = query(f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")[0]
    if not row:
        return redirect("/login")

    resp = redirect("/")
    resp.set_cookie("user_id", str(row[0][0]) + "-" + create_hash(str(row[0][0])))
    return resp


if __name__ == "__main__":
    init()
    app.run()
```

### Solusi

Dengan membuka link [challenge](http://challenges.ctf.compfest.id:20003), didapatkan halaman web: 

![Main page](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-14%20234128.png)

Kemudian setelah meng-klik tombol login, didapatkan halaman login:  

![Login page](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-14%20234135.png)

Source code python dari website menggunakan sql sebagai database, kemungkinan besar dapat kita lakukan sql injection pada laman login.

Untuk membuktikannya mari perhatikan dua fungsi berikut:
```python
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return redirect("/login")

    row = query(f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")[0]
    if not row:
        return redirect("/login")

    resp = redirect("/")
    resp.set_cookie("user_id", str(row[0][0]) + "-" + create_hash(str(row[0][0])))
    return resp

@app.get("/")
def index():
    valid, user = parse_cookie(request.cookies.get("user_id", ""))
    if not valid:
        user = "Guest"

    bottom = "<a href='/login'>Login</a>"
    if user != "Guest":
        row = query("SELECT username, is_admin FROM users WHERE id = ?", [user])[0]
        if row:
            user = row[0][0]
            bottom = "<a href='/logout'>Logout</a>"
            if row[0][1] == 1:
                bottom += f"<p>Flag: {FLAG}</p>"
        else:
            user = "Guest"

    return f"<p>Hello, {user}.</p>{bottom}"
```
Fungsi process_login() dipanggil saat kita melakukan submit pada halaman login. Fungsi akan melakukan query sql dengan statement:
```sql
SELECT id FROM users WHERE username = '{username}' AND password = '{password}'
```

Input dari user untuk query tidak di validasi sehingga bisa saja langsung dilakukan sql injection. Namun, ada syarat tambahan yang perlu kita lakukan.

Pada fungsi index(), terlihat bahwa flag akan ditampilkan jika row[0][1] = 1. row sendiri merupakan hasil dari query sql yang mengambil column 'username' dan 'is_admin' dari user yang memiliki id = user_id.

Sementara 'user_id' adalah cookies yang didapat dari proses login, artinya 'user_id' ditetapkan setelah kita melakukan login.

> row[0] : hasil query dari user pertama yang memenuhi kondisi (kemungkinan ada lebih dari satu user)  
> row[0][0] : username dari user pertama yang memiliki id = user_id  
> row[0][1] : nilai 'is_admin' dari user pertama yang memiliki id = user_id

Sehingga kesimpulannya, agar flag ditampilkan kita harus login dengan akun yang memiliki nilai 'is_admin' = 1.

Maka akan kita masukkan payload injection ke password, username dapat diisi string apa saja selain string kosong. Payload yang sesuai yaitu:
```sql
' OR '1' AND is_admin = '1
```

> **Note:** Username tidak boleh string kosong karena ada pengecekan pada process_login(), jika username atau password kosong maka akan otomatis login dengan user 'guest'.

Jika kita masukkan payload ke query di fungsi process_login(), maka query akan menjadi:
```sql
SELECT id FROM users WHERE username = '(random_string)' AND password = '' OR '1' AND is_admin = '1'
```

Query tersebut dapat disederhanakan menjadi hanya:
```sql
SELECT id FROM users WHERE is_admin = '1'
```

Sehingga setelahnya, didapat halaman web yang menampilkan flag:  
![Flag](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-15%20074855.png)

> Flag: **COMPFEST16{aLw4Ys_uS3_pr3P4reD_st4tEm3NTS_e3ae331a90}**
