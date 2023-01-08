import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Random väljer något från listan.
    while '-' in word or ' ' in word: # När den loopar, finns mellan eller sträck fortsätt gissa.
        word = random.choice(words) # Stoppar iterera, när den inte har - eller ' '.

    return word.upper() # Den ger oss tillbaka alla våran letter stora bokstäver.


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letter in the word.
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Tom set följa vad spelaren gissar.

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, ' lives left and you have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:  # Om ordet finns i wordletter tabort den i userletter.
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # Takes away a life if wrong
                print('Letter is not in word.')


        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()

user_input = input('Type something: ')
print(user_input)