import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
turtle.penup()
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_answers = []
while len(correct_answers) < 50:
    answer_state = screen.textinput(f"{len(correct_answers)}/50 States Correct", "What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in states:
            if state not in correct_answers:
                states_to_learn.append(state)

        data_file = pandas.DataFrame(states_to_learn)
        data_file.to_csv("missed_states.csv")
        break
    if answer_state in states:
        city = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(city.x), int(city.y))
        t.write(answer_state, False, align="center", font=("Arial", 8, "normal"))
        correct_answers.append(answer_state)

