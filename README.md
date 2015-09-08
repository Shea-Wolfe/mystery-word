# Getting Started
* To run mystery_word.py on the command line enter $ python mystery_word.py
* To run mystery_word_test.py on the command line enter $ python mystery_word_test.py
* To run evil_mystery_word.py on the command line enter $ python evil_mystery_word.py
## Description

mystery_word is a program that uses player guesses to slowly reveal a word.  If they can get the word before they guess 8 letters wrong they win!  

The game first determines the player difficulty with an input of e,m, or h, ignoring inputs besides those.  Then it makes a list with words of a given length based on difficulty from the computer dictionary at /usr/share/dict/words.  Then it selects a word from that list using the random.choice() method.

The game then goes into the main loop, asking for a letter input, checking that it's not a repeat or more than one letter, then checking the letter against the word and leting the player know if the letter is in the word.  This loops until the player gets all the letters or runs out of guesses.  

After the main game loop breaks the player is congratulated or consoled and asked if they want to play again.  If they answer yes or y the game restarts, if they answer anything else the game quits.

Evil_mystery_word has the same base but after every guess the computer makes a dictionary of lists based on that guesses position in the word.  It than picks the list in the dictionary that has the most options and selects a new random word from it.  only after this does it check to see if the player guess is in the word.

## Known Issues

evil_mystery_word requires refining as it currently runs slower and slower as you increase the number of guesses.

The new functions in evil_mystery_word do not have a testing suite built yet.
