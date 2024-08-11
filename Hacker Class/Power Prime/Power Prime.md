# [500 pts] Power Prime
### Category: Cryptography

**Deskripsi:**  
RSA warmup.

Author: swusjask

**chall.py:**
```python
from Crypto.Util.number import getPrime, bytes_to_long
from secret import message, x, y

p = getPrime(y)
n = p ** x
e = 0x10001
c = pow(bytes_to_long(message), e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

# output
# n = 174398141961264126560505296048651397103940625972358808906187816452656090815275082092703206639204234732453380366400438429846076789218559828669690390572528240520254507036152659026582129125892087219537071916257813880120391483891236016422449795410600212796367274254070440928882993348666993424943717023976062255483456283318813107003678274274454583252439764631805477342477492425052659593801
# e = 65537
# c = 38415069832658278102412940476349224522223117826717864236716063942465292251639452037471899276433883280487660575851320701796429668476551053062015248611453285019543570394965516221325993414456754832832080360042304547277452474428650298929639938371072386565545457564351801474854761480051602266412901190322297685878637385354294132832534425751762322767659303351614194618177802401960510283943
```

### Solusi:

Python script melakukan generasi public key (n,e) dan ciphertext (c) dari RSA. Berdasarkan teori RSA, ciphertext didapat dari:
```
c ≡ m ^ e mod n  
m : plaintext
```

Maka kita harus mencari private key (d,e), dimana d didapat dari:
```
d ≡ e ^ -1 mod ϕ(n)
ϕ(n) : banyak bilangan bulat x (1 ≤ x ≤ n) yang relatif prima dengan n
```

ϕ(n) atau biasa disebut totient(n) dapat kita cari melalui integer factorization online tools, misalnya: https://www.alpertron.com.ar/ECM.HTM. 

Dengan memasukkan n dan mengklik tombol "factor". Didapatkan totient(n):
```
ϕ(n) = 174398141961264126560505296048651397103113850339729866335354823879473879278813952850699901097692377993311532672020284272605641707760709058698175264955612734220518692478226386010939885755666007222877097524740258881248144908999743142640875737907117720461851784163293585744916264308981276047682675859838393885230326843327400708242731685800795830053312945075454272054734015647324633957430
```

Kemudian kita masukkan n, ϕ(n), e, dan c ke RSA Decoder online: https://www.dcode.fr/rsa-cipher. 
Pilih opsi display "Plaintext As Character string" dan decrypt:

![RSA Decoder](https://github.com/FieryBanana101/COMPFEST-16_TeamBaruBelajarCTF/blob/main/asset/Screenshot%202024-08-11%20105910.png)

Didapatkan plaintext sebagai string yaitu:
```
m = kripto ez lah ya!! COMPFEST16{genie_genie_a_little_prime_exponent_ez_lah_ya_e78770dfec}
```

Flag terdapat pada plaintext tersebut.
> Flag: **COMPFEST16{genie_genie_a_little_prime_exponent_ez_lah_ya_e78770dfec}**
