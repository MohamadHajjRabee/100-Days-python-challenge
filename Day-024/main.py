# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt", mode="r") as letter_name:
    names = letter_name.readlines()


with open("input/Letters/starting_letter.txt", mode="r") as letter:
    lines = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = lines.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)
