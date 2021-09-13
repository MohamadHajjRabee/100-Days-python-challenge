from random import randint
from art import logo


def check_number(number, user_guess):
    if user_guess > number:
        print("Too high.")
        return False
    elif user_guess < number:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {number}.")
        return True


number = randint(1, 100)


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

end_the_game = False
while not end_the_game:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    end_the_game = check_number(number, user_guess)
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        end_the_game = True
    else:
        print("Guess again.")
