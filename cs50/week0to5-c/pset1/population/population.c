#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_size, end_size;

    // Prompt for start size above 9
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // Prompt for end size which is higher than the start size
    do
    {
        end_size = get_int("End size: ");
    }
    while (start_size > end_size);

    // Calculate number of years until we reach threshold
    int years = 0;

    while (start_size < end_size)
    {
        int newborns = start_size / 3;
        int deaths = start_size / 4;
        start_size = start_size + newborns - deaths;
        years++;
    }

    // Print number of years
    printf("Years: %i\n", years);
}