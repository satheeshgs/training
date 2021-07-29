#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc == 1)
    {
        printf("Hello world!\n");
        return 0;
    }
    else
    {
        printf("Hello %s\n", argv[1]);
        return 0;
    }
}