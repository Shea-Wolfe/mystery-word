import random
import sys
def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_list = []
    for word in word_list:
        if len(word) > 3 and len(word) < 7:
            easy_list.append(word)
        else:
            pass
    return easy_list


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_list = []
    for word in word_list:
        if len(word) > 5 and len(word) < 9:
            medium_list.append(word)
        else:
            pass
    return medium_list


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_list = []
    for word in word_list:
        if len(word) > 7:
            hard_list.append(word)
        else:
            pass
    return hard_list


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return word_list[random.randint(0, len(word_list))]



def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    current_word = (' '.join('_'*len(word))).split()
    count = 0
    for letter in word:
        if letter in guesses:
            current_word[count] = letter
            count += 1
        else:
            count += 1

    return ' '.join(current_word).upper()
# word = 'thiswords'
# blanks = ' '.join('_'*len(word)).split()
# print(blanks)
# letters = 'tis'
# count = 0
#
# for letter in word:
#     if letter in letters:
#         blanks[count] = letter
#         count += 1
#     else:
#         count += 1
# final_word = ' '.join(list_word)
# print(final_word)
# print(type(final_word))
# print(blanks)
# ' '.join(blanks)






def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    current_word = (' '.join('_'*len(word))).split()
    count = 0
    for letter in word:
        if letter in guesses:
            current_word[count] = letter
            count += 1
        else:
            count += 1
    if "_" not in ' '.join(current_word):
        return True
    else:
        return False


def get_difficulty(user_input):
    if difficulty == 'quit':
        sys.exit()
    elif difficulty == 'e' or difficulty == 'easy':
        return 'e'
    elif difficulty == 'n' or difficulty == 'normal' or difficulty == 'm' or difficulty == 'medium':
        return 'n'
    elif difficulty == 'h' or difficulty == 'hard':
        return 'h'
        return get_difficulty

def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    while True:
        difficulty = input('Please enter a difficulty [E]asy, [N]ormal, or [H]ard.  At any time type QUIT to quit.> ').lower())
        if difficulty not in 'enh' or len(difficulty) != 1:
            print('That\'s not a valid difficulty!')
            continue
        elif difficulty == 'e':
            computer_word_list = easy_words(word_list)
            break
        elif difficulty == 'n':
            computer_word_list = medium_words(word_list)
            break
        elif difficulty == 'h':
            computer_word_list = hard_words(word_list)
            break
    computer_word = random_word(computer_word_list)
    strikes = 8
    player_guesses = ''
    print('Word has {} letters'.format(len(computer_word)))
    while strikes <= 0 or is_word_complete(computer_word, player_guesses) == False:
        print(display_word(computer_word, player_guesses)) #remember to fix
        print(strikes)
        print(' '.split(player_guesses.join())
        player_letter = player_guess()
        letters.replace(player_letter,'')
        guessed_letters.append(player_letter)
        if player_letter in computer_word:
            print('That\'s in the word!')
            print('you have {} guesses remaining!'.format(strikes))
            popped_letters = []
            for letter in computer_word:
                if letter == player_letter:
                    #figure out how to get the index
                    #set the index of word_display to = the letter.
        else:
            strikes -=1
            print('Sorry, that\'s not in the word!)
            print('you have {} guesses remaining!'.format(strikes))
            pass #print out _ _ _ map
    if strikes <= 0:
        credit = input('Sorry, you lose. Word was {}  Try again? [y]/[n]'.format(computer_word))
        if credit == 'y' or credit == 'yes':
            return game()
        else:
            sys.exit()
    else:
        credit = input('Congratulations!  You\'ve won! Play again? [y]/[n]')
        if credit == 'y' or credit == 'yes':
            return game()
        else:
            sys.exit()


if __name__ == '__main__':
    main()
