#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv, char** envp) {
    char rdx = 6;
    int64_t file;
    __builtin_memcpy(&file, "\x7f\x63\x75\x4c\x43\x45\x03\x54\x06\x59\x50\x68\x43\x5f\x04\x68\x54\x03\x5b\x5b\x02\x4a\x37", 0x17);

    for (int32_t i = 0; i <= 0x16; i = (i + 1)) {
        uint8_t *ptr = (uint8_t*)(&file + i);
        *ptr = (*ptr ^ 0x37);
    }
    int32_t fd = open((char*)&file, O_RDONLY, rdx);
    if (fd > 0) {
        puts("[*] Box Opened Successfully");
        close(fd);
    } else {
        puts("[X] Error: Box Not Found");
    }
    return 0;
}
