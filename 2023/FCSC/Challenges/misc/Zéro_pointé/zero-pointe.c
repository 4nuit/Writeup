#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


static void
flag(int sig)
{
    (void) sig;
    char flag[128];

    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    int n = read(fd, flag, sizeof(flag));
    if (n == -1) {
        perror("read");
        exit(EXIT_FAILURE);
    }

    flag[n] = 0;
    flag[strstr(flag, "\n") - flag] = 0;

    if (close(fd) == -1) {
        perror("close");
        exit(EXIT_FAILURE);
    }

    printf("%s\n", flag);

    exit(EXIT_SUCCESS);
}

long
read_long()
{
    long val;
    scanf("%ld", &val);
    return val;
}

int
main()
{
    long a;
    long b;
    long c;

    if (signal(SIGFPE, flag) == SIG_ERR) {
        perror("signal");
        exit(EXIT_FAILURE);
    }

    a = read_long();
    b = read_long();
    c = b ? a / b : 0;

    printf("%ld\n", c);
    exit(EXIT_SUCCESS);
}
