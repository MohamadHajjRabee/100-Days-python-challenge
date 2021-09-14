from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def switch_card():
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")


def generate_word():
    global current_card, skip_time
    current_card = random.choice(data)
    window.after_cancel(skip_time)
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    skip_time = window.after(3000, func=switch_card)


def known_word():
    data.remove(current_card)
    generate_word()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
skip_time = window.after(3000, func=switch_card)
try:
    with open("data/words_to_learn.csv", "r") as data_file:
        file = pandas.read_csv(data_file)
        data = pandas.DataFrame.to_dict(file, orient="records")

except FileNotFoundError:
    with open("data/french_words.csv", "r") as data_file:
        file = pandas.read_csv(data_file)
        data = pandas.DataFrame.to_dict(file, orient="records")


canvas = Canvas(width=800, height=526)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=1)

generate_word()
window.mainloop()

data_file = pandas.DataFrame(data)
data_file.to_csv("data/words_to_learn.csv", index=False)
