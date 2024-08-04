# [500 pts] magik
### Category: Web Exploitation

**Deskripsi**
>i can do magik you know ^^
>
>Author: mone
>
>http://challenges.ctf.compfest.id:20002
__________________________________________________________________________________________________________

Di berikan URL website dan file PHP yang berasal dari source website:
```HTML
<html>
    <body>
        <div>
            <?php 
            if (isset($_GET['secret'])) {
                if ($_GET['secret'] !== "240610708" && md5($_GET['secret']) == "0e462097431906509019562988736854" && $_GET['secret'] !== "3069655" && md5($_GET['secret']) == "0e731198106197620485820904131008") {
                    echo "REDACTED";
                } else {
                    echo "Invalid secret!";
                }
            } else {
                echo "Please specify secret in the GET parameter!";
            }
            ?>
        </div>
    </body>

    <style>
        div {
            display: flex;
            align-items: center; /* vertically center the div element */
            justify-content: center; /* horizontally center the div element */
            width: 100%; 
            height: 100%; 
            text-align: center;
            margin: 0 auto; /* center the div element horizontally */
        }
    </style>
</html>
```

Dari source website terdapat kode PHP yang mengecek string query dari parameter metode GET yang bernama secret, namun ada kondisi yang menggunakan loose comparison (**==**). 
Loose comparison PHP hanya mengecek value dan tidak mengecek type. Sehingga:
>(== "0e462097431906509019562988736854") berubah menjadi (== 0)  
>(== "0e731198106197620485820904131008") berubah menjadi (== 0)

Maka untuk memenuhi kondisi itu, kita hanya perlu mengisi parameter metode GET dengan string yang bukan merupakan "240610708" dan bukan "3069655" serta nilai hash MD5 nya berawalan "0".
Setelah mencari di internet, ditemukan list [magic hash](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md) yang berisi nilai yang kita butuhkan, yaitu "QNKCDZO".

Dengan menambahkan string "QNKCDZO" pada parameter secret metode GET, akan didapatkan flag.
>http://challenges.ctf.compfest.id:20002/?secret=QNKCDZO

>Flag = **COMPFEST16{1_h4T3_pHp_lmA000000_8da795d09f}**
