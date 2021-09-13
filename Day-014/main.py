from typing import Sequence
import art
from data import data
from random import choice
import os


def clear():
    return os.system('cls')


def compare(A_followers, B_followers, user_guess):
    if A_followers > B_followers:
        winner_person = "A"
    else:
        winner_person = "B"
    if user_guess == winner_person:
        return True
    else:
        return False


print(art.logo)
score = 0
end_the_game = False
person_A = choice(data)
while not end_the_game:

    person_B = choice(data)
    print(
        f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
    print(art.vs)
    print(
        f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    resault = compare(person_A["follower_count"],
                      person_B["follower_count"], user_guess)
    clear()
    print(art.logo)
    if resault == True:
        score += 1
        print(f"You're right! Current score: {score}")
        person_A = person_B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_the_game = True
