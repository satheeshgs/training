#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // Get card number input from the user; no spaces, special characters or alphabets allowed
    long card_number = get_long("Number: ");


    // Initializing other variables used in the code
    int i = 0;
    int array[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int length_of_card, sum_array = 0;
    int validity = 0;


    // extracting the card digits and storing them in an array
    do
    {
        array[i] = card_number % 10;
        card_number = card_number / 10;
        //printf("%i   %ld   %i\n", array[i], card_number, i);
        i++;
    }
    while (card_number > 0);

    // Set the total length of the card and the first digit
    length_of_card = i;
    int first_digit = array[length_of_card - 1];
    int second_digit = array[length_of_card - 2];


    // Rejecting invalid cards using card length
    if (length_of_card < 13 || length_of_card > 16)
    {
        validity = 0;
        printf("INVALID\n");
    }
    // Luhn's algorithm if the card length is valid
    else
    {
        // Luhn's algorithm implementation:
        for (int j = 0; j < length_of_card; j++)
        {
            if (j % 2 != 0) //doubling only every other digit starting with the tens place
            {
                array[j] = array[j] * 2;

                if (array[j] >= 10) // adding only the digits rather than the number itself if the value is not single digit
                {
                    array[j] = array[j] / 10 + array[j] % 10;
                }
            }
            sum_array = sum_array + array[j];
        }


        // Determine validity of the card
        if (sum_array % 10 == 0)
        {
            validity = 1;
        }


        // Determine type of card - VISA, MASTERCARD or AMEX
        if (validity == 0)
        {
            printf("INVALID\n");
        }

        //AMEX card identification
        else if (validity == 1 && first_digit == 3 && length_of_card == 15)
        {
            if (second_digit == 4 || second_digit == 7)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        //MASTERCARD card identification
        else if (validity == 1 && first_digit == 5 && length_of_card == 16)
        {
            if (second_digit == 1 || second_digit == 2 || second_digit == 3 || second_digit == 4 || second_digit == 5)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        //VISA card identification
        else if (validity == 1 && first_digit == 4)
        {
            if (length_of_card == 13 || length_of_card == 16)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
    }

}