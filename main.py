import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ALLIGNMENT = "center"
FONT = ("Courier", 12, "bold")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
player_score = 0
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"States Guessed: {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        learn_list = pandas.DataFrame(missing_states)
        learn_list.to_csv("missing_states.csv")
        screen.exitonclick()
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        answer_row = data[data.state == answer_state]
        answer_cord_x = answer_row.x
        answer_cord_y = answer_row.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(answer_cord_x),int(answer_cord_y))
        t.write(arg=f"{answer_state}", move=False, align=ALLIGNMENT, font=FONT)
        player_score += 1

turtle.mainloop()
