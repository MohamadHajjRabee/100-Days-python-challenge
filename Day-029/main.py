from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_website = web_entry.get()
    user_email = email_entry.get()
    user_pass = pass_entry.get()

    if len(user_website) == 0 or len(user_pass) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: "
                                                                   f"\nEmail: {user_email} \n Password: {user_pass} "
                                                                   f"\nIs it ok to save?")

        if is_ok:

            file = open("data.txt", "a")
            file.write(f"{user_website} | {user_email} | {user_pass}\n")
            file.close()
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=("Arial", 10, "bold"))
web_label.grid(row=1, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
web_entry.focus()

email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "test@gmail.com")

pass_label = Label(text="Password:", font=("Arial", 10, "bold"))
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="ew")

pass_gen_button = Button(text="Generate Password", command=generate_password)
pass_gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
