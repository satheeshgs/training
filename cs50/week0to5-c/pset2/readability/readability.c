#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

string format_lower(string text);
int find_words(string text);
int find_sentences(string text);
int find_letters(string text);


int main(void)
{
    // Get input text from user
    string user_text;
    do
    {
        user_text = get_string("Text: ");
    }
    while (strlen(user_text) == 0);

    string formatted_text = format_lower(user_text);
    //printf("lower text: %s\n", formatted_text);


    // Find the number of words, sentences and letters in the user text
    int words = find_words(formatted_text);
    //printf("Word count: %i\n", words);

    int letters = find_letters(formatted_text);
    //printf("Letter count: %i\n", letters);

    int sentences = find_sentences(formatted_text);
    //printf("Sentence count: %i\n", sentences);

    // Calculating necessary l and s values
    float l = (float) letters / words * 100.00; // calculate letters per 100 words
    //printf("Letters per 100 words: %f\n", l);
    float s = (float) sentences / words * 100.00; // calculate sentences per 100 words
    //printf("Sentences per 100 words: %f\n", s);

    // Use the coleman index formula
    int grade = round(0.0588 * l - 0.296 * s - 15.8);


    // Output the index to the user
    if (grade < 16 && grade > 1)
    {
        printf("Grade %i\n", grade);
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
}


string format_lower(string text)
{

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        text[i] = tolower(text[i]);
    }
    return text;
}


int find_words(string text)
{
    // Find the number of words in the text
    int counter = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }

    return counter;

}

int find_sentences(string text)
{
    // Checking for valid string
    int length = strlen(text);
    if (length == 0)
    {
        return 0;
    }

    // Find the number of words in the text

    int counter = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            counter++;
        }
    }

    if (counter == 0) // in case there are no punctuations, setting the value of counter to 1
    {
        counter = 1;
    }
    return counter;
}

int find_letters(string text)
{
    // Checking for valid string
    int length = strlen(text);
    if (length == 0)
    {
        return 0;
    }


    // TODO: Find the number of letters in the text
    int counter = 0;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            counter++;
        }
    }
    return counter;
}