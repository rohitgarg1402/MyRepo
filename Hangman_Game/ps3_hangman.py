
import random
import string

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
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count1 = 0
    for i in secretWord:
        if i in lettersGuessed:
            count1 += 1
    if count1 == len(secretWord):
        return True
    else: 
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    list1 = []
    for i in secretWord:
        if i in lettersGuessed:
            list1.append(i)
        else:
            list1.append("_")

    return list1



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    list1 = []
    for lett in string.ascii_lowercase:
        if lett not in lettersGuessed:
            list1.append(lett)
    return "".join(list1)
    


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

    '''
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long"
    print "---------------------"
    guesses = []
    printlist = []
    count = 8

    list2 = []
    for i in range(0,len(secretWord)):
        list2.append("_")

    while(count > 0):
        print "You have " +str(count) + " guesses left."
        letters = getAvailableLetters(guesses)
        print "Available letters:",letters
        guesses.append(raw_input("Please guess a letter:")) # Focus on changing values of 
                                                            # returnValofGGW somehow

        returnValofGGW = getGuessedWord(secretWord,guesses)

        for t in range(0,len(returnValofGGW)):
            if returnValofGGW[t] in secretWord:
                list2[t] = returnValofGGW[t] 
        
        flag = 0
        
        for i in returnValofGGW:
            if guesses[-1] == i:
                flag = 1
                break
            else:
                flag = 3


        for val in range(0,len(guesses)-1):
            if guesses[val] == guesses[-1]:
                flag = 2

        if flag == 2:
            print "Oops! You've already guessed that letter", " ".join(list2)
            print "---------------------"
            count += 1

        elif flag == 3:   
            print "Oops! That letter is not in my word: "," ".join(list2)
            print "---------------------"


        elif flag == 1:
            print "Good Guess: "," ".join(list2)
            print "---------------------"
            count += 1

        result = isWordGuessed(secretWord, guesses)

        if result == True:
            print "Congratulations, you won!"
            break

        count -= 1

        if(count == 0):
            print "Sorry, you ran out of guesses. The word was else."
            break

hangman('hello')

    

# uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


