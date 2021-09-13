from tkinter import *


def converter():
    miles = float(user_input.get())
    label3["text"] = miles * 1.609


window = Tk()
window.minsize(width=350, height=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

user_input = Entry(width=10)
user_input.grid(row=1, column=2)

font = ("Arial", 15, "normal")
label1 = Label(text="Miles", font=font)
label1.grid(row=1, column=3)
label1.config(padx=10, pady=10)


label2 = Label(text="is equal to", font=font)
label2.grid(row=2, column=1)

km = 0
label3 = Label(text=km, font=font)
label3.grid(row=2, column=2)
label3.config(padx=10, pady=10)

label4 = Label(text="Km", font=font)
label4.grid(row=2, column=3)

button = Button(text="Calculate", command=converter)
button.grid(row=3, column=2)

window.mainloop()
