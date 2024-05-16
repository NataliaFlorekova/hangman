import nltk
import random
import playground as pg

nltk.download("wordnet")

from nltk.corpus import wordnet
from more_itertools import locate


#creating word database for the Hangman
def word_database():
    with open("/usr/share/dict/words", "r") as words_database:
        words = words_database.read().split()

    #keeping only nouns longer than 2 characters without punctuation mark
    nouns = list(filter(lambda word: wordnet.synsets(word, pos=wordnet.NOUN) and len(word) > 2 and '\'' not in word, words))
    return nouns


#printing current state of guessing
def print_current_state(pg):
    for letter in pg.guess_state:
        
        if letter == ' ':
            print('_ ', end='')
        
        else:
            print(f"{letter} " , end='')
    print()


#validating user input
def get_and_validate_guess(already_tried):
    while True:    
        guess = input("Enter your guess: ").upper()
        is_valid_guess = len(guess) == 1 and ord(guess) >= ord('A') and ord(guess) <= ord('Z')
        
        if guess in already_tried:
            print(f"{guess} has been already tried, try again")
            continue
        
        if is_valid_guess:
            already_tried.add(guess)
            return guess
        
        print("Invalid letter, try again")


#evaluating checked guess
def evaluate_guess(pg, word, guess):
    located = list(locate(word, lambda x: x == guess))
    
    if not located:
        pg.incorrect_guess()
        return

    for i in located:
        pg.guess_state[i] = guess


#the whole Hangman game
def play():
    words = word_database()
    selected_word = words[random.randrange(0, len(words))].upper()
    playground = pg.Playground(selected_word)
    is_guessed = False
    already_tried = set()
    
    while playground.incorrect < 7:
        print(''.join(playground.hangman))
        print_current_state(playground)
        guess = get_and_validate_guess(already_tried)
        evaluate_guess(playground, selected_word, guess)
        
        if ''.join(playground.guess_state) == selected_word:
            is_guessed = True
            print(f"You guessed the correct word: {selected_word}!")
            return 
    
    print(''.join(playground.hangman))
    print(f"You wasted all of your attempts\nGiven word was {selected_word}")


if __name__ == "__main__":
    play()
