import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getWordScore(word, n):
    SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    sum = 0
    for i in word:
        sum = sum + SCRABBLE_LETTER_VALUES[i]

    sum = sum * len(word)

    if len(word) == n:
        sum = sum + 50
    return sum



def updateHand(hand, word):
    hand1 = hand.copy()
    for i in word:
        hand1[i] = hand1[i] - 1
    return hand1

def isValidWord(word, hand, wordList):
    flag = False
    if len(word) == 0:
        return flag
    hand1 = hand.copy()
    if word in wordList:
        for i in word:
            if i in hand1.keys():
                #print hand1
                if hand1[i] > 0:
                    flag = True
                    hand1[i] = hand1[i] - 1
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    else:
        flag = False
    #print hand
    return flag

def calculateHandlen(hand):
    length = 0
    for key in hand:
        length = length + hand[key]
    return length

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,     # print all on the same line 

def playHand(hand, wordList, n):
    points = 0
    len_of_hand = calculateHandlen(hand)
    while(1):
        # Condition if there is no letters left
        if n == 0:
            print "Run out of letters. Total score: " + str(points) + " points."
            break
        # till here
        print "Current Hand: ",
        displayHand(hand)
        word = raw_input('\nEnter word, or a "." to indicate that you are finished: ')
        if word == ".":
            print "Goodbye! Total score: " + str(points) + " points."
            break

        valid_or_not = isValidWord(word, hand, wordList)

        if valid_or_not == False:
            print "Invalid word, please try again.\n"

        else:
            n = n - len(word)
            total_points = getWordScore(word,len_of_hand)
            points = points + total_points
            print word + " earned " + str(total_points) + " points. " + " Total: " + str(points) + " points\n"
            hand = updateHand(hand, word)

def dealHand(n):
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def playGame(wordList):

    HAND_SIZE = 8
    flag = False
    hand = dealHand(HAND_SIZE)
    wordlist = loadWords()
    while(1):
        print '\n'
        letter = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if letter == 'r':
            if flag == False:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                playHand(hand,wordlist,len(HAND_SIZE))
        elif letter == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordlist,len(HAND_SIZE))
            flag = True

        elif letter == 'e':
            break

        else:
            print "Invalid Command\n"


letters = loadWords()
playGame(letters)




#
# Build data structures used for entire session and play game
#


               
