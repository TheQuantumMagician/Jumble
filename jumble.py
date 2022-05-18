#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# jumble.py
# A Jumble word solver.
# 2022-05-16 @TheQuantumMage
#

import itertools

# The Jumble letters
letters = []

# See if the current test word is a real word in the dictionary
# NOTE: Probably better to open the file once, outside of this routine,
# and then just keep searching the already cleaned list.
def findMatch(test):
    # Open our word list file
    with open("words_lowercase.txt") as words:
        # Read the file line by line, which is also word by word
        for word in words.readlines():
            # Strip white space, including \r and \n, so we have just the word to work with
            cleanWord = word.strip()
            # Does the test word match our current word?
            if cleanWord == test:
                print(cleanWord)

# Create a list of letters for the input jumbled word
letters = []
while (len(letters) < 1):
    # Ask for input
    rawJumble = input("Please enter the jumbled word: ")
    # Remove any non-letters
    jumble = rawJumble.strip()
    # End the program if no input
    if (len(jumble) == 0):
        exit()
    # Convert the word into a list of letters
    for jum in jumble:
        letters.append(jum)

# Create a place to keep track of what permutations we've already tested
tested = []
# Create a list of the possible permutations of the list of letters
for word in list(itertools.permutations(letters, len(letters))):
    # create a word from the current permutation of letters
    test = ""
    for let in word:
        test += let
    # Make sure we filter out duplicate permutations.
    # For example, bboona has 4 duplicate permutations because of
    # duplicate letters. All we need to test is the one baboon.
    if (test not in tested):
         # See if its in the dictionary
         findMatch(test)
         tested.append(test)
