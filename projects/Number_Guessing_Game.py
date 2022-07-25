from os import system as clear
from random import *
from ancii_art.logo_guess_the_number import logo
clear('cls')


def calculate(you_resp, computer_number):
    """
    Retorna:
        -1 se you_resp for menor que computer_number;
        -1 se you_resp for maior que computer_number;
    Caso contrário:
        'You got it' -  se for you_resp adivinhar o número do computer_number. 
    """
    if you_resp < computer_number:
        print("Too low.")
        return - 1

    elif you_resp > computer_number:
        print("Too High")
        return - 1
    else:
        print(f"You got it! The answer was {computer_number}")
        
def game_start():
    computer_number = randint(1, 101)
    attempts = 0
    wins = False

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psss, a resposta correta é {computer_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while not wins:
        print(f"You have {attempts} attempts remaining to guess the number.")
        resp = int(input("Make a guess: "))

        result = calculate(resp, computer_number)

        if attempts > 1:
            if result == -1:
                print("Guess again.")
                attempts += result
            else:
                wins = True
        else:
            print("You've run out of guesses, you lose.")
            wins = True

game_start()

