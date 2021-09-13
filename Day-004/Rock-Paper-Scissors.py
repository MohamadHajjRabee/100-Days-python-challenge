import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all = [rock, paper, scissors]
user_chose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(all[user_chose])
print("Computer chose:")
computer = random.randint(0, 2)
print(all[computer])

if (user_chose == 0 and computer == 2) or (user_chose == 2 and computer == 1) or (user_chose == 1 and computer == 0):
    print("You win!")
elif user_chose == computer:
    print("Draw!")
else:
    print("You lose.")
