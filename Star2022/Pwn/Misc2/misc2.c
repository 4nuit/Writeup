#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//gcc -o misc2 misc2.c -no-pie -m32

void vuln(){
        puts("I like trains");
        sleep(1);
        system("sl");
}

void main(){
        setregid(getegid(), getegid());
        vuln();
}
