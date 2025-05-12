import turtle
import pandas

# Setup screen and image
screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 50
correct_answer = 0

FONT = ("Courier", 8, "bold")
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
all_guessed_state = []


# Writer turtle setup
writer = turtle.Turtle("circle")
writer.pu()
writer.hideturtle()

game_on = True
while game_on:

    # Get user input
    answer_state = screen.textinput(
        title=f"{correct_answer}/{score} States correct",
        prompt="What's  another state name? "
               "(Type 'Exit' to quit): ").title()

    if not answer_state: # Skip if no input
        continue

    # Exit condition
    if answer_state == "Exit":
        break


# Check if the guessed state is correct and not already guessed
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

# List of missing states
missing_states = [state for state
                      in all_state if state not in
                      all_guessed_state]

# Create a DataFrame using the two lists (correct and missed)

for state in missing_states:
    state_data = data[data.state == state]
    x = state_data.x.item()
    y = state_data.y.item()
    writer.goto(x, y)
    writer.write(state, align="center",
                 font=FONT)

# Padding the shorter list with None to match the length
max_length = max(len(all_guessed_state), len(missing_states))
all_guessed_state.extend([None] * (max_length -
            len(all_guessed_state)))  # Pad with None

missing_states.extend([None] * (max_length -
            len(missing_states)))  # Pad with None

# Create a DataFrame using the two lists (correct and missed)
new_data = {
    "states you missed":missing_states,
    "states you guessed right":all_guessed_state,
    }

df = pandas.DataFrame(new_data)
df.to_csv("all_missed_states.csv", index=False)


# Game over message
writer.goto(0, 0)
if len(all_guessed_state) == 50:
    writer.write("Game Over!\nYou guessed all 50 states!",
                 align="center", font=("Courier", 18, "bold"))
else:
    writer.write("Game Over!\nBetter luck next time.",
                 align="center", font=("Courier", 18, "bold"))

screen.exitonclick()