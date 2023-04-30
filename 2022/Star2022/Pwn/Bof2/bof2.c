#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

//gcc -o bof2 bof2.c -no-pie -fno-stack-protector -m32 -z execstack

void shell(){
 setregid(getegid(), getegid());
 system("/bin/sh");
}

void vuln(){
 char buffer[50];
 puts("What can gorfou see from the moon?");
 gets(buffer);
}

void main(){
 vuln();
}
