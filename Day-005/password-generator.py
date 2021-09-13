import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create random letters
ps_letters = []
for n in range(nr_letters):
    letter = random.randint(0, len(letters) - 1)
    ps_letters += letters[letter]

# Create random symbols
ps_symbols = []
for n in range(nr_symbols):
    symbol = random.randint(0, len(symbols) - 1)
    ps_symbols += symbols[symbol]

# Create random numbers
ps_numbers = []
for n in range(nr_numbers):
    number = random.randint(0, len(numbers) - 1)
    ps_numbers += numbers[number]

# Add all the letters and symbols and numbers together and then random them
ps_final = ps_letters + ps_symbols + ps_numbers
random_ps_final = ""
for n in range(0, len(ps_final)):
    ps = random.randint(0, len(ps_final) - 1)
    random_ps_final += ps_final[ps]
    ps_final.pop(ps)

print(f"Your password is: {random_ps_final}")
