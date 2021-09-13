from art import logo


def caeser(ttext, tshift, tdirection):
    result = ""
    if tdirection == "decode":
        tshift *= -1
    for letter in ttext:
        if letter in alphabet:
            letter_index = alphabet.index(letter)

            index_of_the_letter = letter_index + tshift
            index_of_the_letter %= 26

            one_letter = alphabet[index_of_the_letter]
        else:
            one_letter = letter
        result += one_letter
    print(f"Here's the {tdirection}d result: {result}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

continue_caesering = True
while continue_caesering:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    asking_user = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if asking_user == "no":
        print("Goodbye")
        continue_caesering = False
