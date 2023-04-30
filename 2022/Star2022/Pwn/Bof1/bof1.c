#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

//gcc -o bof1 bof1.c -no-pie -fno-stack-protector -m32 -z execstack

void vuln(){
        int i;
        int win = 0;
        char buffer[40];
        puts("Can the gorfou fly?");
        fgets(buffer, 44, stdin);
        if(win){
                puts("Fly gorfou, reach the moooooon!");
                setregid(getegid(), getegid());
                system("/bin/sh");
        }
        else {
                puts("I guess not :(");
        }
}

void main(){
        vuln();
}
