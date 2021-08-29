import re


def main():
    # get input text from user
    user_text = input("Text: ")

    # call functions to get number of sentences, words and letters in the text
    s = sentences(user_text)
    l = letters(user_text)
    words = word_count(user_text)

    # sentences and letters per 100 words
    s = s / words * 100
    print("s: " + str(s))
    l = l / words * 100
    print("l: " + str(l))

    # calculate coleman lieu index
    index = 0.0588 * l - 0.296 * s - 15.8

    # print the necessary indexstyle50 readability.py
    if index > 1 and index < 16:
        print(f"Grade {round(index)}")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade 16+")


def sentences(text):
    '''
    returns the number of sentences per 100 words
    input: text
    output: sentences in the text
    '''
    return len(re.split(r'[.!?]+', text)) - 1


def letters(text):
    '''
    returns the number of letters per 100 words
    input: text
    output: number of letters in text without puncutations and spaces
    '''
    letter_count = 0
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(" ", "")

    return len(text)


def word_count(text):
    '''
    returns the word count of a text
    input: user text
    output: count of words in text

    '''
    return len(text.split())
    

if __name__ == "__main__":
    main()