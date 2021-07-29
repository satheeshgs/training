#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Converting the string key argument into integer

    string key = argv;
    printf("%s\n", key);

    string plain_text;

    // Getting the plain text from the user
    do
    {
        plain_text = get_string("plaintext: ");
    }
    while (strlen(plain_text) == 0);

    int n = strlen(plain_text);

    // Converting to cipher text
    for (int i = 0; i < n; i++)
    {
        //printf("%i  ", plain_text[i]);

        if (isupper(plain_text[i]))
        {
            plain_text[i] = (plain_text[i] + key - 65) % 26 + 65; // ASCII for A is 65
        }
        else if (islower(plain_text[i]))
        {
            plain_text[i] = (plain_text[i] + key - 97) % 26 + 97; // ASCII for a is 97
        }

        //printf("%i\n", plain_text[i]);
    }

    // print out the cipher text
    printf("ciphertext: %s\n", plain_text);
    return 0;
}