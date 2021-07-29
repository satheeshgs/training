#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // Get change owed from the user
    float dollars;
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars < 0);

    // Converting the dollars into cents
    int cents = round(dollars * 100);

    // Initializing the cents array which will be used as part of the greedy algorithm
    int coins = 0;
    int array[4] =  {25, 10, 5, 1};

    // Greedy algorithm
    for (int i = 0; i < 4; i++)
    {
        coins = coins + cents / array[i];
        cents = cents % array[i];
    }

    printf("%i\n", coins);

}