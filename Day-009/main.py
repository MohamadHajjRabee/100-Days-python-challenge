from logo import logo
import os


def clear():
    return os.system('cls')


print(logo)
Infos = {}

continue_bidding = True
while continue_bidding:
    username = input("What is your name?: ")
    userbid = int(input("What is your bid?: $"))

    Infos[username] = userbid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == 'yes':
        clear()
    else:
        continue_bidding = False

highest_bid = 0
for key in Infos:
    if Infos[key] > highest_bid:
        highest_bid = Infos[key]
        winner_user = key

print(f"The winner is {winner_user} with a bid of ${highest_bid}")
