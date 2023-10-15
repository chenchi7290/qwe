#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<sys/wait.h>

int main(int argc, char *argv[])
{
    printf("hello world (pid:%d)\n", (int)getpid());

    int rc = fork();
    if (rc < 0)
    {
        fprintf(stderr, "fork failed\n");
        exit(1);
    }
    else if (rc == 0)
    {
        printf("hello, I am child (pid:%d)\n", (int)getpid());
    }
    else
    {
        int wc=wait(NULL);
        printf("hello, I am parent of %d (pid:%d)\n", rc, (int)getpid());
    }
    return 0;
}