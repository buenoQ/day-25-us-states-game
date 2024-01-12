import turtle
from turtle import Turtle
import pandas

FONT = ('Arial', 9, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
us_states = list(data.state)

writer = Turtle()
writer.hideturtle()
writer.penup()


game_score = 0
while len(us_states) > 0:

    answer_state = screen.textinput(title=f"{game_score}/50 States Correct", prompt="What's another states name?")
    answer_state = answer_state.title()

    if answer_state in us_states:
        state_value = data[data.state == answer_state]
        writer.goto(state_value.x.iloc[0], state_value.y.iloc[0])
        writer.write(f"{answer_state}", False, "center", FONT)
        game_score += 1
        us_states.remove(answer_state)

    elif answer_state == "Exit":
        break

# states to learn
# get the list that has only states; whatever is remaining in that list turn to a dictionary and then convert that into
# a dataframe and then that into a csv

remaining_states_dict = {
    "state": us_states
}

remaining_states_df = pandas.DataFrame(remaining_states_dict)
remaining_states_df.to_csv("states_to_learn.csv")
