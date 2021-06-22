# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord) <= set(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join(char if char in lettersGuessed else '_' for char in secretWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join(char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in lettersGuessed)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Entering the Hangman game!
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")

    #Setting the total number of guesses and the intial variables
    guessesLeft = 8
    lettersGuessed = []
    wordGuess = getGuessedWord(secretWord, lettersGuessed)

    #game to continue when the guesses is not 0 or the word is not guessed yet
    while isWordGuessed(secretWord, lettersGuessed) is False:
      print("You have "+str(guessesLeft)+" guesses left") #number of guesses being shown to the user
      print("Available Letters: "+getAvailableLetters(lettersGuessed))
      userGuess = input("Please guess a letter: ") #getting the user guess and appending to the list
      if userGuess in lettersGuessed:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        print("-----------")
      else: 
        lettersGuessed.append(userGuess)
        
      #TODO: see if the guessed letter is in the secret word; if its in secret word, 
      # then the word is shown with filled letters, 
      # else reduce guess by 1
        if userGuess in list(secretWord):
          print("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
          print("-----------")
        else:
          guessesLeft -= 1
          print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
          print("-----------")
          if guessesLeft == 0:
            print("Sorry, you ran out of guesses. The word was " +secretWord)
            return  # exit when the guesses becomes zero and the word is not guessed yet

    print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
