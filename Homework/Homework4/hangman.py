import random

from helpers import *

word = random.choice(words)

allowed_errors = 3
guesses = []
done = False
if __name__ == '__main__':
    print ("Welcome to Hangman!")
    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print('')

        guess = input(f'Allowed mistakes left {allowed_errors}, \nTake a guess: ')
        guesses.append(guess.lower())
        if guess.lower == word.lower:
            break
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False


    if done:
        print('You won!The word was ',word)
    else:
        print('You lost!The word was ',word)