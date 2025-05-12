import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 50
correct_answer = 0

FONT = ("Courier", 8, "bold")
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list
all_guessed_state = []

writer = turtle.Turtle("circle")
writer.pu()
writer.hideturtle()

game_on = True
while game_on:

    answer_state = screen.textinput(
        title=f"{correct_answer}/{score} States correct",
        prompt="What's  another state name? "
               "(Type 'Tired' to quit): ").title()

    if not answer_state:
        continue

    answer_state = answer_state.title().strip()

    if answer_state == "Tired":
        break

    if (answer_state in all_state and answer_state
            not in all_guessed_state):
        correct_answer+=1
        all_guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        writer.goto(x= x_cor, y= y_cor)
        writer.write(arg= answer_state,
                     align= "center", font= FONT)

missing_states = [state for state
                      in all_state if state not in
                      all_guessed_state]

for state in missing_states:
    state_data = data[data.state == state]
    x = int(state_data.x)
    y = int(state_data.y)
    writer.goto(x, y)
    writer.write(state, align="center",
                 font=FONT)

# Game over message
writer.goto(0, 0)
if len(all_guessed_state) == 50:
    writer.write("Game Over!\nYou guessed all 50 states!",
                 align="center", font=("Courier", 18, "bold"))
else:
    writer.write("Game Over!\nBetter luck next time.",
                 align="center", font=("Courier", 18, "bold"))

screen.exitonclick()