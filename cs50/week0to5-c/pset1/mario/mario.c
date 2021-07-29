#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get user input from 1 to 8
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);


    // print the pyramid
    for (int i = 1; i <= n; i++)
    {
        // printing the first pyramid
        for (int j = n - i; j > 0; j--)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // two spaces between the pyramids
        printf("  ");

        // printing the second pyramid
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        printf("\n");

    }

}