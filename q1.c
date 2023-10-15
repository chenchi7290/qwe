#include <stdio.h>

int main()
{
    int x = 42;
    int rc = fork();
    printf("Parent pid: %d\n",(int)getpid());
    if (rc == 0)
    {
        printf("New: x=%d\n",x);
        printf("New: rc=%d\n",rc);
        printf("New pid: %d\n",(int)getpid());
    }
    else
    {
        printf("Old: x=%d\n",x);
        printf("Old: rc=%d\n",rc);
        printf("Old pid: %d\n",(int)getpid());
    }
}
