// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table using frequency of letters (https://en.wikipedia.org/wiki/Letter_frequency) and ascii values
const unsigned int N = 10810;

// Hash table
node *table[N];

//dictionary size;
unsigned int size_of_dict;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // hash the word
    int hash_value = hash(word);

    //get to specific linked list
    node *cursor = table[hash_value];

    //stroll through linked list
    while (cursor != NULL)
    {
        if (strcasecmp(cursor -> word, word) == 0)
        {
            return true;
        }

        cursor = cursor -> next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // calculating the hash value using ascii values addition
    // using the division method from https://www.educba.com/hashing-function-in-c/
    int len = strlen(word);
    long sum = 0;

    for (int i = 0; i < len; i++)
    {
        sum =  sum + tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // fopen to open the file using file pointer
    FILE *dict = fopen(dictionary, "r");

    if (dict == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }

    char new_word[LENGTH + 1];

    //read the next word from the dictionary and repeat till EOF
    while (fscanf(dict, "%s", new_word) != EOF)
    {
        //create a new node using malloc
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return false;
        }

        strcpy(n -> word, new_word); //copy string using strcopy

        //hash function to hash the new word
        int hash_value = hash(new_word);

        //insert into hash table location
        n -> next = table[hash_value];
        table[hash_value] = n;
        size_of_dict++;

    }
    //closind dictionary pointer
    fclose(dict);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (size_of_dict != 0)
    {
        return size_of_dict;
    }

    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //memory deallocation
    for (int i = 0; i < N; i++)
    {
        //pointing to i'th linked list
        node *cursor = table[i];

        while (cursor != NULL)
        {
            //temp pointer
            node *tmp = cursor;

            //point cursor to next
            cursor = cursor -> next;

            //free temp pointer
            free(tmp);
        }

        //returning true only if cursor is null at the last index
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }


    return false;
}
