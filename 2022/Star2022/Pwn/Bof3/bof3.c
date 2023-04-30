#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

//gcc -o bof3 bof3.c -no-pie -fno-stack-protector -m32 -z execstack

void vuln(){
        char buffer[50];
        printf("Cadeau: %p\n",buffer);
        puts("What does the gorfou say, now?");
        gets(buffer);
}

void main(){
        setregid(getegid(), getegid());
        vuln();
}
