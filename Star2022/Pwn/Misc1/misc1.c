#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//gcc -o misc1 misc1.c -no-pie -m32

void vuln(){
        char* filename;
        char buffer[60];
        puts("which file do you want to read?");
        fgets(buffer, 60, stdin);
        buffer[strcspn(buffer, "\n")] = '\0';
        
	if(strstr(buffer, "flag")){
                puts("No way!");
                exit(0);
        }
        FILE *fp = fopen(buffer, "r");
        if(fp){
                fgets(buffer,sizeof(buffer),fp);
                printf("%s\n",buffer);
        }
        else{
                puts("Cannot open file.");
        }
}

void main(){
 vuln();
}
