import hangman_art
import hangman_words
import random

print(hangman_art.logo)

word = random.choice(hangman_words.word_list)
display = []
for i in range(len(word)):
    display.append("_")

lives = 6
end_the_game = False
while not end_the_game:
    guess = input("Guess a letter :").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess

    print(f"{' '.join(display)}")

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    print(hangman_art.stages[lives])
    if "_" not in display:
        print("You win")
        end_the_game = True
    elif lives == 0:
        print("You lose.")
        end_the_game = True
