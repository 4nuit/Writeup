## Code

Il suffit de fournir autre chose qu'un nombre ...

```c
        else if(atoi(buf)>4){
            printf("That's not an option\n");
            exit(0);
    }

    print_flag();
```

## Solution

```bash
┌─[night@night-20b7s2ex01]─[~/buckeyectf/pwn/beginner_menu]
└──╼ 4 fichiers, 32Kb)─$ nc chall.pwnoh.io 13371
Enter the number of the menu item you want:
1: Hear a joke
2: Tell you the weather
3: Play the number guessing game
4: Quit
A
bctf{y0u_ARe_sNeaKy}
```
